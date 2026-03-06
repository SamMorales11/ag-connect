from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

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
    date_of_birth = Column(String, nullable=True) # [BARU] Format YYYY-MM-DD
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    attendances = relationship("Attendance", back_populates="owner")

class Attendance(Base):
    __tablename__ = "attendances"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id")) 
    scan_time = Column(DateTime(timezone=True), server_default=func.now())
    
    owner = relationship("User", back_populates="attendances")