from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship # [BARU] Untuk membuat relasi antar tabel

from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    whatsapp = Column(String)
    status = Column(String)
    talents = Column(String)
    qr_code_data = Column(String, unique=True, index=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # [BARU] Relasi: 1 User bisa memiliki banyak data Absensi (Attendance)
    attendances = relationship("Attendance", back_populates="owner")

# ==========================
# [BARU] TABEL ABSENSI
# ==========================
class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    # ForeignKey ini adalah "tali" yang mengikat absensi ke ID jemaat tertentu
    user_id = Column(Integer, ForeignKey("users.id")) 
    
    # Otomatis mencatat tanggal & jam persis saat QR di-scan
    scan_time = Column(DateTime(timezone=True), server_default=func.now())
    
    # Relasi balik untuk mengenali siapa pemilik absensi ini
    owner = relationship("User", back_populates="attendances")