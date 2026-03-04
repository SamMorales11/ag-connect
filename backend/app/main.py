from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
import bcrypt
import jwt
from jwt.exceptions import InvalidTokenError # [BARU] Untuk menangani error token
import uuid
from datetime import datetime, timedelta

from . import models, schemas, database

# Perintah ajaib untuk otomatis membuat tabel
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="AG Connect API")

# ==========================
# KONFIGURASI KEAMANAN & JWT
# ==========================
SECRET_KEY = "kunci_rahasia_ag_connect_sangat_aman_123!" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7 # Token berlaku 7 hari

# Ini yang memunculkan tombol "Authorize" (Gembok) di Swagger UI
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

def verify_password(plain_password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_password_hash(password: str) -> str:
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_password.decode('utf-8')

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ==========================
# [BARU] FUNGSI CEK USER SAAT INI (BERDASARKAN TOKEN)
# ==========================
def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token tidak valid atau sudah kadaluarsa",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        # Buka isi token JWT
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except InvalidTokenError:
        raise credentials_exception
        
    # Cari user di database berdasarkan username di dalam token
    user = db.query(models.User).filter(models.User.username == username).first()
    if user is None:
        raise credentials_exception
    return user


# ==========================
# 1. ENDPOINT REGISTER
# ==========================
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
        qr_code_data=qr_data
    )
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# ==========================
# 2. ENDPOINT LOGIN
# ==========================
@app.post("/login", response_model=schemas.Token)
def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    user = db.query(models.User).filter(models.User.username == form_data.username).first()
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Username atau password salah",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
    access_token = create_access_token(data={"sub": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

# ==========================
# 3. [BARU] ENDPOINT PROFIL SAYA (RAHASIA/TERKUNCI)
# ==========================
@app.get("/users/me", response_model=schemas.UserResponse)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    # Fungsi ini hanya bisa diakses jika jemaat membawa Token yang valid.
    # Secara otomatis mengembalikan biodata user yang sedang login (termasuk qr_code_data).
    return current_user