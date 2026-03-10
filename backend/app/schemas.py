from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class UserBase(BaseModel):
    fullname: str
    username: str
    whatsapp: Optional[str] = None
    status: Optional[str] = None
    talents: Optional[str] = None
    date_of_birth: Optional[str] = None # Menyimpan tanggal lahir

class UserCreate(UserBase):
    password: str 

class UserResponse(UserBase):
    id: int
    qr_code_data: Optional[str] = None
    is_admin: bool  
    created_at: datetime

    class Config:
        from_attributes = True

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class AttendanceBase(BaseModel):
    pass

class AttendanceCreate(AttendanceBase):
    qr_code_data: str
    service_type: str = "AG"

class AttendanceResponse(AttendanceBase):
    id: int
    user_id: int
    scan_time: datetime

    class Config:
        from_attributes = True

class UserForAttendance(BaseModel):
    fullname: str
    status: str
    
    class Config:
        from_attributes = True

# ==========================================
# [DIPERBAIKI] FORMAT DATA UNTUK DASHBOARD
# ==========================================
class AttendanceListResponse(BaseModel):
    id: int
    scan_time: datetime
    service_type: Optional[str] = "AG" # [BARU] Menambahkan tipe ibadah
    user: UserForAttendance              # [DIPERBAIKI] Diubah dari 'owner' menjadi 'user'

    class Config:
        from_attributes = True