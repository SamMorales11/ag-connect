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

# --- [BARU] CEK REFERRAL ---
@app.get("/users/check-referral/{username}")
def check_referral(username: str, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == username.lower()).first()
    if not user: raise HTTPException(status_code=404)
    return {"valid": True, "fullname": user.fullname.split()[0]}

# --- [REVISI] REGISTER DENGAN POIN ---
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

# --- [REVISI] SCAN DENGAN POIN ---
@app.post("/scan")
def scan_attendance(request: schemas.AttendanceCreate, db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.qr_code_data == request.qr_code_data).first()
    if not user: raise HTTPException(status_code=404)
    user.points += 5
    db.add(models.Attendance(user_id=user.id, service_type=request.service_type))
    db.commit()
    return {"message": "Berhasil"}

@app.get("/users", response_model=List[schemas.UserResponse])
def get_users(db: Session = Depends(get_db)):
    return db.query(models.User).all()