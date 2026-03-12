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
from . import models, schemas, database

class ScanRequestData(BaseModel):
    qr_code_data: str
    service_type: str = "AG"

models.Base.metadata.create_all(bind=database.engine)
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
        if username is None: raise credentials_exception
    except InvalidTokenError: raise credentials_exception
        
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None: raise credentials_exception
    return user

# --- ENDPOINT REFERRAL ---
@app.get("/users/check-referral/{username}")
def check_referral(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username).first()
    if not user: raise HTTPException(status_code=404, detail="Username tidak ditemukan")
    return {"valid": True, "fullname": user.fullname.split()[0]}

# --- REGISTER DENGAN LOGIKA POIN ---
@app.post("/register", response_model=schemas.UserResponse)
def register_jemaat(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user: raise HTTPException(status_code=400, detail="Username sudah terdaftar")
    
    initial_points = 0
    valid_referrer = None
    
    if user.referred_by:
        referrer_db = db.query(models.User).filter(models.User.username == user.referred_by).first()
        if referrer_db:
            valid_referrer = referrer_db.username
            initial_points = 2
            referrer_db.points += 2
            db.add(referrer_db)

    new_user = models.User(
        fullname=user.fullname,
        username=user.username,
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
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    # Mencari user berdasarkan username (Pastikan input sesuai DB)
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Username atau password salah")
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

@app.get("/users/me", response_model=schemas.UserResponse)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

# --- SCAN DENGAN LOGIKA POIN ---
@app.post("/scan")
def scan_attendance(request: ScanRequestData, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.qr_code_data == request.qr_code_data).first()
    if not user: raise HTTPException(status_code=404, detail="QR Code tidak valid")
    
    user.points += 5 # Tambah 5 poin saat hadir
    db.add(user)

    new_attendance = models.Attendance(user_id=user.id, service_type=request.service_type)
    db.add(new_attendance)
    db.commit()
    return {"message": "Absensi dicatat", "scan_time": new_attendance.scan_time}

# --- ENDPOINT LAINNYA ---
@app.get("/attendance/logs")
def get_attendance_logs(db: Session = Depends(get_db)):
    return db.query(models.Attendance).options(joinedload(models.Attendance.user)).order_by(models.Attendance.scan_time.desc()).all()

@app.get("/users", response_model=List[schemas.UserResponse])
def get_all_users(db: Session = Depends(get_db)):
    return db.query(models.User).order_by(models.User.created_at.desc()).all()