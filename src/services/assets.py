from src.services.base import BaseService
from src.db.models import Assets
from src.db.session import create_session
from sqlalchemy.orm import Session
from src.schema.assets import AddAsset, Asset
from typing import Any

class AssetsService(BaseService[Assets, AddAsset, Any]):
    def __init__(self, db_session: Session):
        super().__init__(Assets, db_session)
    
    def create(self, obj: AddAsset) -> str:
        id = self.generate_id()
        asset_obj = Asset(
            id=id,
            **obj.dict()
        )
        super().create(asset_obj)
        return id

def get_assets_service():
    # session = get_session()
    session = create_session()
    return AssetsService(session)