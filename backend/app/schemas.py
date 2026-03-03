from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# ==========================
# SCHEMAS UNTUK USER (JEMAAT)
# ==========================

# 1. Skema dasar yang memuat field umum
class UserBase(BaseModel):
    fullname: str
    username: str
    whatsapp: Optional[str] = None
    status: Optional[str] = None
    talents: Optional[str] = None

# 2. Skema saat registrasi (butuh password)
class UserCreate(UserBase):
    password: str 

# 3. Skema respon data user (Tanpa password!)
class UserResponse(UserBase):
    id: int
    qr_code_data: Optional[str] = None
    is_admin: bool
    created_at: datetime

    class Config:
        from_attributes = True # Dulu orm_mode = True, penting untuk membaca data dari SQLAlchemy