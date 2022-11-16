from pydantic import BaseModel
from typing import Any, Optional
from datetime import datetime

class Asset(BaseModel):
    id : str
    description : Optional[str] = ""
    owner : str
    price : int
    for_sale : bool = True
    asset_url : Optional[str]
    timestamp = datetime.utcnow()
    class Config:
        orm_mode = True

class AddAsset(BaseModel):
    description : str
    owner : str
    price : int
    for_sale : bool = True
    asset_url : Optional[str]


