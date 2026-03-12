from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String, index=True)
    username = Column(String, unique=True, index=True)
    password_hash = Column(String)
    whatsapp = Column(String, nullable=True)
    status = Column(String, nullable=True)
    talents = Column(String, nullable=True)
    date_of_birth = Column(String, nullable=True)
    qr_code_data = Column(String, unique=True, index=True)
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    points = Column(Integer, default=0)
    referred_by = Column(String, nullable=True)

    # [BARU] Relasi balik ke tabel Attendance
    # cascade="all, delete-orphan" artinya jika user dihapus, data absensinya juga ikut terhapus otomatis
    attendances = relationship("Attendance", back_populates="user", cascade="all, delete-orphan")


class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    scan_time = Column(DateTime(timezone=True), server_default=func.now())
    service_type = Column(String, default="AG")

    # [BARU] Relasi ke tabel User agar FastAPI bisa memanggil log.user.fullname
    user = relationship("User", back_populates="attendances")