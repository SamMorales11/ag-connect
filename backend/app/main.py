from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session, joinedload
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import bcrypt
import jwt
from jwt.exceptions import InvalidTokenError
import uuid
from datetime import datetime, timedelta
from typing import List, Optional
import csv
from io import StringIO
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import func 
from . import models, schemas, database

app = FastAPI(title="AG Connect API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

SECRET_KEY = "kunci_rahasia_ag_connect_sangat_aman_123!" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def get_password_hash(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None: raise HTTPException(status_code=401)
    except: raise HTTPException(status_code=401)
    user = db.query(models.User).filter(models.User.username == username).first()
    return user

@app.get("/users/check-referral/{username}")
def check_referral(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username.lower()).first()
    if not user: raise HTTPException(status_code=404)
    return {"valid": True, "fullname": user.fullname.split()[0]}

@app.post("/register", response_model=schemas.UserResponse)
def register_jemaat(user: schemas.UserCreate, db: Session = Depends(get_db)):
    if db.query(models.User).filter(models.User.username == user.username.lower()).first():
        raise HTTPException(status_code=400, detail="Username sudah terdaftar")
    
    initial_points = 0
    valid_referrer = None
    if user.referred_by:
        ref = db.query(models.User).filter(models.User.username == user.referred_by.lower()).first()
        if ref:
            valid_referrer = ref.username
            initial_points = 2
            ref.points += 2
            db.add(ref)

    new_user = models.User(
        fullname=user.fullname,
        username=user.username.lower().replace(" ", ""),
        password_hash=get_password_hash(user.password),
        whatsapp=user.whatsapp,
        status=user.status,
        talents=user.talents,
        date_of_birth=user.date_of_birth,
        qr_code_data=str(uuid.uuid4()),
        points=initial_points,
        referred_by=valid_referrer
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@app.post("/login", response_model=schemas.Token)
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username.lower().strip()).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Salah kredensial")
    return {"access_token": jwt.encode({"sub": user.username, "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)}, SECRET_KEY, algorithm=ALGORITHM), "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.UserResponse)
def read_me(current_user: models.User = Depends(get_current_user)):
    return current_user

@app.post("/scan")
def scan_attendance(request: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.qr_code_data == request.qr_code_data).first()
    if not user: raise HTTPException(status_code=404, detail="QR Code tidak valid")
    
    today_date = datetime.utcnow().date()
    
    sudah_absen_hari_ini = db.query(models.Attendance).filter(
        models.Attendance.user_id == user.id,
        func.date(models.Attendance.scan_time) == today_date
    ).first()

    pesan_notifikasi = ""
    layanan_tanpa_poin = ["Doa Fajar", "Doa Pengerja", "AGC/Fellowship"]

    if request.service_type in layanan_tanpa_poin:
        pesan_notifikasi = "Hadir (Acara ini tidak mendapat Poin)"
    else:
        if not sudah_absen_hari_ini:
            user.points += 5
            db.add(user)
            pesan_notifikasi = "Berhasil! +5 Poin Gamifikasi"
        else:
            pesan_notifikasi = "Kehadiran dicatat (Sudah mendapat poin hari ini)"

    new_attendance = models.Attendance(user_id=user.id, service_type=request.service_type)
    db.add(new_attendance)
    db.commit()
    
    return {"message": pesan_notifikasi, "fullname": user.fullname}

@app.get("/users", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()

@app.get("/attendance/logs")
def get_attendance_logs(
    page: int = 1, 
    limit: int = 20,
    service_type: Optional[str] = None,
    search: Optional[str] = None,
    date_filter: Optional[str] = None,
    db: Session = Depends(get_db)
):
    query = db.query(models.Attendance).options(joinedload(models.Attendance.user))
    
    # 1. Filter Kategori Ibadah
    if service_type and service_type != 'Leaderboard':
        query = query.filter(models.Attendance.service_type == service_type)
        
    # 2. Filter Tanggal
    if date_filter:
        query = query.filter(func.date(models.Attendance.scan_time) == date_filter)
        
    # 3. Filter Pencarian Nama
    if search:
        query = query.join(models.User).filter(models.User.fullname.ilike(f"%{search}%"))
        
    # 4. Hitung Total Data (Untuk Paginasi Frontend)
    total_count = query.count()
    
    # 5. Potong Data Sesuai Halaman (Paginasi Server-Side)
    skip = (page - 1) * limit
    logs = query.order_by(models.Attendance.scan_time.desc()).offset(skip).limit(limit).all()
    
    return {
        "total": total_count,
        "page": page,
        "limit": limit,
        "data": logs
    }

@app.post("/users/{user_id}/add-quiz-points")
def add_quiz_points(user_id: int, db: Session = Depends(get_db), current_admin: models.User = Depends(get_current_user)):
    if not current_admin.is_admin:
        raise HTTPException(status_code=403, detail="Akses ditolak. Hanya Admin yang dapat memberikan poin kuis.")
    
    target_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not target_user:
        raise HTTPException(status_code=404, detail="Jemaat tidak ditemukan")
    
    target_user.points += 10
    db.add(target_user)
    db.commit()
    
    return {"message": f"🎉 10 Poin Kuis berhasil dikirim ke {target_user.fullname}!"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db), current_admin: models.User = Depends(get_current_user)):
    if not current_admin.is_admin:
        raise HTTPException(status_code=403, detail="Akses ditolak. Hanya Admin yang dapat menghapus data.")
        
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Jemaat tidak ditemukan")
    
    db.delete(user)
    db.commit()
    return {"message": "Data jemaat berhasil dihapus"}

@app.put("/users/{user_id}/promote")
def promote_user(user_id: int, db: Session = Depends(get_db), current_admin: models.User = Depends(get_current_user)):
    if not current_admin.is_admin:
        raise HTTPException(status_code=403, detail="Akses ditolak. Hanya Admin yang dapat melakukan promosi.")
        
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="Jemaat tidak ditemukan")
    
    user.is_admin = True
    db.add(user)
    db.commit()
    return {"message": "Jemaat berhasil diangkat menjadi Admin"}

@app.put("/users/reset-points")
def reset_all_points(db: Session = Depends(get_db), current_admin: models.User = Depends(get_current_user)):
    if not current_admin.is_admin:
        raise HTTPException(status_code=403, detail="Akses ditolak. Hanya Admin yang dapat mereset poin.")
    
    db.query(models.User).update({models.User.points: 0}, synchronize_session=False)
    db.commit()
    
    return {"message": "Semua poin jemaat berhasil direset ke 0! Musim baru siap dimulai."}

# --- [MAHAKARYA BARU] FUNGSI EXPORT DATA BENTUK MATRIKS DENGAN AUTO-FORMAT EXCEL ---
@app.get("/export/attendances")
def export_attendances(filter: str = 'all', service_type: str = 'Semua', db: Session = Depends(get_db), current_admin: models.User = Depends(get_current_user)):
    if not current_admin.is_admin:
        raise HTTPException(status_code=403, detail="Akses ditolak. Hanya Admin yang dapat mengekspor laporan.")
    
    query = db.query(models.Attendance).options(joinedload(models.Attendance.user))
    
    if service_type != 'Semua':
        query = query.filter(models.Attendance.service_type == service_type)
        
    now = datetime.utcnow()
    if filter == 'today':
        today_start = now.replace(hour=0, minute=0, second=0, microsecond=0)
        query = query.filter(models.Attendance.scan_time >= today_start)
    elif filter == 'week':
        week_start = now - timedelta(days=7)
        query = query.filter(models.Attendance.scan_time >= week_start)
    elif filter == 'month':
        month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
        query = query.filter(models.Attendance.scan_time >= month_start)
        
    # Ambil log yang sudah difilter
    logs = query.order_by(models.Attendance.scan_time.asc()).all()
    
    si = StringIO()
    
    # [TRIK RAHASIA] Memaksa Excel membaca koma sebagai pemisah kolom secara otomatis
    si.write("sep=,\n")
    
    cw = csv.writer(si, delimiter=',')
    
    if not logs:
        cw.writerow(["Tidak ada data kehadiran untuk kriteria ini."])
        # Tambahkan BOM agar karakter terbaca sempurna oleh Excel
        return Response(content='\ufeff' + si.getvalue(), media_type="text/csv")

    # 1. Temukan Tanggal Unik (Untuk dijadikan Kolom ke kanan)
    unique_dates = sorted(list(set(log.scan_time.date() for log in logs)))
    date_headers = [d.strftime("%d %b %Y") for d in unique_dates]
    
    # 2. Buat Header Tabel (Pojok Kiri)
    headers = ["Nama Jemaat", "Kategori", "Total Hadir"] + date_headers
    cw.writerow(headers)
    
    # 3. Kelompokkan data absensi berdasarkan ID Jemaat
    attendance_map = {}
    for log in logs:
        if log.user_id not in attendance_map:
            attendance_map[log.user_id] = set()
        attendance_map[log.user_id].add(log.scan_time.date())
        
    # 4. Tampilkan semua Jemaat yang terdaftar di sistem
    all_users = db.query(models.User).order_by(models.User.fullname).all()
    
    for user in all_users:
        user_dates_present = attendance_map.get(user.id, set())
        
        # Susun baris awal: Nama, Kategori, Total Hadir
        kategori_user = user.status if user.status else "-"
        row = [user.fullname, kategori_user, len(user_dates_present)]
        
        # Beri tanda "v" jika hadir di tanggal tersebut, "-" jika absen
        for d in unique_dates:
            if d in user_dates_present:
                row.append("v") # Hadir
            else:
                row.append("-") # Tidak Hadir
                
        cw.writerow(row)
        
    # Gabungkan BOM (\ufeff) dengan isi CSV agar Excel tidak salah membaca format
    output_string = '\ufeff' + si.getvalue()
    return Response(content=output_string, media_type="text/csv")