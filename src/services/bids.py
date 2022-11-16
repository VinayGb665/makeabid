from src.services.base import BaseService
from src.db.models import Bids
from src.schema.bids import BidStatus, Bid, AddNewBid
from sqlalchemy.orm import Session
from sqlalchemy import func
from src.db.session import create_session
from typing import Any, List
class BidsService(BaseService[Bids, AddNewBid, Any]):
    def __init__(self, db_session: Session):
        super().__init__(Bids, db_session)

    def create(self, obj: AddNewBid) -> str:
        current_max_bid = self.get_highest_bid_for_an_asset(obj.asset_id)
        if obj.quote_price < current_max_bid :
            raise Exception("Quote is less than the current max bid")
        id = self.generate_id()
        bid_obj = Bid(
            id=id,
            **obj.dict()
        )
        super().create(bid_obj)
        return id
    
    def list_bids_for_an_asset(self, asset_id: str) -> List[Bid]:
        bids_db_objs: List[Bids] = self.db_session.query(self.model).filter(
            Bids.asset_id.like(asset_id)
        )
        bids: List[Bid] = []
        for obj in bids_db_objs:
            bids.append(
                Bid.from_orm(obj)
            )
        return bids
    
    def list_bids_for_an_user(self, user_id: str) -> List[Bid]:
        bids_db_objs: List[Bids] = self.db_session.query(self.model).filter(
            Bids.bidder.like(user_id)
        )
        bids: List[Bid] = []
        for obj in bids_db_objs:
            bids.append(
                Bid.from_orm(obj)
            )
        return bids
    
    def list_bids_for_an_asset_by_user(self, user_id: str, asset_id: str) -> List[Bid]:
        bids_db_objs: List[Bids] = self.db_session.query(self.model).filter(
            Bids.bidder.like(user_id),
            Bids.asset_id.like(asset_id)
        )
        bids: List[Bid] = []
        for obj in bids_db_objs:
            bids.append(
                Bid.from_orm(obj)
            )
        return bids 
    
    def get_highest_bid_for_an_asset(self, asset_id: str) -> int | None:
        query = f"""select max(quote_price) from bids where asset_id='{asset_id}'; """
        highest_bid_obj = self.db_session.execute(
            query
        ).fetchone()
        if highest_bid_obj[0]:
            return highest_bid_obj[0]
        return 0

def get_bids_service():
    session = create_session()
    return BidsService(session)