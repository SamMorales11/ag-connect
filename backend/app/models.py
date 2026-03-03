from sqlalchemy import Boolean, Column, Integer, String, Text, DateTime
from sqlalchemy.sql import func
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(100), nullable=False)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password_hash = Column(Text, nullable=False) # Kita simpan hash-nya, BUKAN password asli
    whatsapp = Column(String(20))
    status = Column(String(50)) # Misal: Mahasiswa, Pekerja
    talents = Column(Text) # Misal: Musik, Multimedia
    qr_code_data = Column(String(100), unique=True, index=True) # UUID untuk QR Code
    is_admin = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())