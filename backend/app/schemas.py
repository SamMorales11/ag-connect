from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# ==========================
# SCHEMAS UNTUK USER (JEMAAT)
# ==========================
class UserBase(BaseModel):
    fullname: str
    username: str
    whatsapp: Optional[str] = None
    status: Optional[str] = None
    talents: Optional[str] = None

class UserCreate(UserBase):
    password: str 

class UserResponse(UserBase):
    id: int
    qr_code_data: Optional[str] = None
    is_admin: bool  # <--- Ini kunci untuk memunculkan tombol di Vue
    created_at: datetime

    class Config:
        from_attributes = True

# ==========================
# SCHEMAS UNTUK AUTENTIKASI (LOGIN)
# ==========================
class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

# ==========================
# SCHEMAS UNTUK ABSENSI
# ==========================
class AttendanceBase(BaseModel):
    pass

class AttendanceCreate(AttendanceBase):
    qr_code_data: str

class AttendanceResponse(AttendanceBase):
    id: int
    user_id: int
    scan_time: datetime

    class Config:
        from_attributes = True

# Cetakan untuk mengambil nama dan status jemaat di Dashboard
class UserForAttendance(BaseModel):
    fullname: str
    status: str
    
    class Config:
        from_attributes = True

# Cetakan gabungan: Data Absen + Data Jemaat
class AttendanceListResponse(BaseModel):
    id: int
    scan_time: datetime
    owner: UserForAttendance 

    class Config:
        from_attributes = True