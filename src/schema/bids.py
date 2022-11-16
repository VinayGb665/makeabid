from pydantic import BaseModel
from typing import Any
from enum import Enum
from datetime import datetime
class BidStatus(Enum):
    placed = 1
    accepted = 2
    failed = 3
    reveresed = 4

class Bid(BaseModel):
    ## TODO: Bid status as of now is str see how we can make it an enum
    id: str
    bidder: str
    asset_id: str
    quote_price: int
    # status: BidStatus = BidStatus.placed
    status: str = "placed"
    timestamp = datetime.utcnow()
    class Config:
        orm_mode = True

class AddNewBid(BaseModel):
    bidder: str
    asset_id : str
    quote_price : int
