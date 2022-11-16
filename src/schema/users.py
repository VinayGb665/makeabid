import hashlib
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: Optional[str]
    verified: Optional[bool]
    hash: str    
    class Config:
        orm_mode = True

class AddUserSchema(BaseModel):

    username: str
    email: Optional[str]
    password: str

    def get_hash(self,):
        return hashlib.md5(f"{self.username}={self.password}".encode("utf-8")).hexdigest()