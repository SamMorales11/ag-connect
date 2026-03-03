from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import bcrypt # Menggunakan bcrypt secara langsung
import uuid

from . import models, schemas, database

# Perintah ajaib untuk otomatis membuat tabel
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="AG Connect API")

# --- FUNGSI HASHING BARU ---
def get_password_hash(password: str) -> str:
    # Ubah string ke byte
    pwd_bytes = password.encode('utf-8')
    # Generate salt (karakter acak tambahan)
    salt = bcrypt.gensalt()
    # Hash password dengan salt
    hashed_password = bcrypt.hashpw(pwd_bytes, salt)
    # Kembalikan sebagai string agar bisa masuk ke database
    return hashed_password.decode('utf-8')
# ---------------------------

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/register", response_model=schemas.UserResponse)
def register_jemaat(user: schemas.UserCreate, db: Session = Depends(get_db)):
    # 1. Cek apakah username sudah dipakai
    db_user = db.query(models.User).filter(models.User.username == user.username).first()
    if db_user:
        raise HTTPException(status_code=400, detail="Username sudah terdaftar")
    
    # 2. Enkripsi password dan buat ID unik untuk QR Code
    hashed_password = get_password_hash(user.password)
    qr_data = str(uuid.uuid4()) 
    
    # 3. Siapkan data
    new_user = models.User(
        fullname=user.fullname,
        username=user.username,
        password_hash=hashed_password,
        whatsapp=user.whatsapp,
        status=user.status,
        talents=user.talents,
        qr_code_data=qr_data
    )
    
    # 4. Simpan ke database
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user