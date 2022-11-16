from pydantic import BaseModel
from datetime import datetime

class Wallet(BaseModel):
    id: str
    owner: str
    balance: int
    escrow_balance: int
    class Config:
        orm_mode = True
    # last_updated =

class NewWallet(BaseModel):
    owner: str
    balance: int = 0
    escrow_balance: int = 0
    last_updated = datetime.utcnow()