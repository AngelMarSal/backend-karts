from pydantic import BaseModel, EmailStr
from typing import Optional


class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class UserInResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    rol: str
    
    class Config:
        # Permite que Pydantic lea datos de objetos ORM (como la clase User)
        from_attributes = True

class LoginResponse(BaseModel):
    token: str
    user: UserInResponse