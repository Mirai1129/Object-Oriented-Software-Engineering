from typing import Optional

from pydantic import BaseModel


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: Optional[str] = None


class UserBase(BaseModel):
    account: str


class StudentCreate(UserBase):
    student_id: str
    name: str
    password: str


class TeacherCreate(UserBase):
    teacher_id: str
    name: str
    password: str
