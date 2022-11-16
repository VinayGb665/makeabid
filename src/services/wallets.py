from src.services.base import BaseService
from src.db.models import Wallets
from src.db.session import create_session
from sqlalchemy.orm import Session
from src.schema.wallets import NewWallet, Wallet
from typing import Any, List

class WalletsService(BaseService[Wallets, Any, Any]):
    def __init__(self, db_session: Session):
        super().__init__(Wallets, db_session)
    
    def create(self, user_id: str):
        id = self.generate_id()
        wallet = Wallet(
            id=id,
            owner=user_id,
            balance=0,
            escrow_balance=0
        )
        super().create(wallet)
        return id
    
    def get_user_wallet(self, user_id: str):
        user_wallet: Wallets = self.db_session.query(self.model).filter(
            Wallets.owner.like(user_id)
        ).first()
        if user_wallet:
            return Wallet.from_orm(user_wallet)
        raise Exception("Invalid user id / wallet was not created")
    

def get_wallets_service():
    session = create_session()
    return WalletsService(session)