from fastapi import FastAPI, Depends, HTTPException, status, Response
from sqlalchemy.orm import Session, joinedload
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
import bcrypt
import jwt
from jwt.exceptions import InvalidTokenError
import uuid
from datetime import datetime, timedelta
from typing import List
import csv
from io import StringIO

from fastapi.middleware.cors import CORSMiddleware

from . import models, schemas, database

class ScanRequestData(BaseModel):
    qr_code_data: str
    service_type: str = "AG"

# Perintah ajaib untuk otomatis membuat tabel
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="AG Connect API")

# ==========================
# PENGATURAN CORS
# ==========================
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Mengizinkan semua origin untuk mencegah error block saat download file
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ==========================
# KONFIGURASI KEAMANAN & JWT
# ==========================
SECRET_KEY = "kunci_rahasia_ag_connect_sangat_aman_123!" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def get_password_hash(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(pwd_bytes, salt).decode('utf-8')

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token tidak valid",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
        
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user


@app.post("/register", response_model=schemas.UserResponse)
def register_jemaat(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar")
    
    hashed_password = get_password_hash(user.password)
    qr_data = str(uuid.uuid4()) 
    
    new_user = models.User(
        fullname=user.fullname,
        username=user.username,
        password_hash=hashed_password,
        whatsapp=user.whatsapp,
        status=user.status,
        talents=user.talents,
        date_of_birth=user.date_of_birth,
        qr_code_data=qr_data
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


@app.post("/login", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username atau password salah")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}


@app.get("/users/me", response_model=schemas.UserResponse)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user


@app.post("/scan")
def scan_attendance(request: ScanRequestData, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.qr_code_data == request.qr_code_data).first()
    if not user:
        raise HTTPException(status_code=404, detail="QR Code tidak valid")
    new_attendance = models.Attendance(user_id=user.id, service_type=request.service_type)
    db.add(new_attendance)
    db.commit()
    db.refresh(new_attendance)
    return {"message": "Absensi dicatat", "scan_time": new_attendance.scan_time, "service_type": new_attendance.service_type}


@app.get("/attendance/logs")
def get_attendance_logs(db: Session = Depends(get_db)):
    logs = db.query(models.Attendance).options(joinedload(models.Attendance.user)).order_by(models.Attendance.scan_time.desc()).all()
    return logs


@app.get("/birthdays", response_model=List[schemas.UserResponse])
def get_birthdays(db: Session = Depends(get_db)):
    users = db.query(models.User).all()
    today_str = datetime.now().strftime("-%m-%d")
    return [u for u in users if u.date_of_birth and u.date_of_birth.endswith(today_str)]


@app.get("/users", response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).order_by(models.User.created_at.desc()).all()


@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    db.delete(db_user)
    db.commit()
    return {"message": "Data dihapus"}


@app.put("/users/{user_id}/promote")
def promote_to_admin(user_id: int, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User tidak ditemukan")
    db_user.is_admin = True
    db.commit()
    return {"message": f"{db_user.fullname} diangkat jadi Admin"}

# ==========================
# ENDPOINT EXPORT LAPORAN CSV (DIUPGRADE DENGAN FILTER)
# ==========================
@app.get("/export/attendances")
def export_attendances(filter: str = "all", db: Session = Depends(get_db), current_user: models.User = Depends(get_current_user)):
    logs = db.query(models.Attendance).options(joinedload(models.Attendance.user)).order_by(models.Attendance.scan_time.desc()).all()
    
    # Memfilter data berdasarkan waktu yang direquest
    filtered_logs = []
    now = datetime.now()
    
    for log in logs:
        if not log.scan_time:
            continue
            
        # Hilangkan zona waktu agar aman saat dibandingkan
        log_date = log.scan_time.replace(tzinfo=None)
        
        if filter == "today":
            if log_date.date() == now.date():
                filtered_logs.append(log)
        elif filter == "week":
            if log_date >= (now - timedelta(days=7)):
                filtered_logs.append(log)
        elif filter == "month":
            if log_date.month == now.month and log_date.year == now.year:
                filtered_logs.append(log)
        else:
            filtered_logs.append(log)

    # Menulis file ke memori sebelum dikirim
    output = StringIO()
    output.write('\ufeff')
    writer = csv.writer(output, delimiter=";")
    
    writer.writerow(["ID Absensi", "Waktu Hadir", "Nama Jemaat", "Status", "Bidang Pelayanan", "Tipe Ibadah"])
    
    for log in filtered_logs:
        time_str = log.scan_time.strftime("%Y-%m-%d %H:%M:%S") if log.scan_time else "-"
        writer.writerow([
            log.id,
            time_str,
            log.user.fullname if log.user else "User Dihapus",
            log.user.status if log.user else "-",
            log.user.talents if log.user else "-",
            log.service_type or "AG"
        ])
        
    response = Response(content=output.getvalue())
    
    # Nama file dinamis mengikuti filter
    suffix = "Semua"
    if filter == "today": suffix = "Hari_Ini"
    elif filter == "week": suffix = "7_Hari_Terakhir"
    elif filter == "month": suffix = "Bulan_Ini"
    
    response.headers["Content-Disposition"] = f"attachment; filename=Laporan_Kehadiran_AG_{suffix}.csv"
    response.headers["Content-Type"] = "text/csv; charset=utf-8"
    return response