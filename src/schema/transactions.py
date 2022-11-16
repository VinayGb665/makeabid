from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime

class Transaction(BaseModel):
    id: str
    seller: str
    buyer: str
    bid_id: str
    ref_url: Optional[str] = ""
    note: Optional[str] = ""
    timestamp = datetime.now()
    class Config:
        orm_mode = True

class NewTransaction(BaseModel):
    seller: str
    buyer: str
    bid_id: str
    ref_url: Optional[str] = ""
    note: Optional[str] = ""
    timestamp = datetime.now()
