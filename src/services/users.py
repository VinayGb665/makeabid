from src.services.base import BaseService
from src.db.models import Users
from src.db.session import get_session, create_session
from sqlalchemy.orm import Session
from src.schema.users import AddUserSchema, User
from typing import Any
class UserService(BaseService[Users, AddUserSchema, Any]):
    def __init__(self, db_session: Session):
        super().__init__(Users, db_session)
    
    def create(self, obj: AddUserSchema) -> Any:
        random_id = self.generate_id()
        user_obj = User(
            id=random_id,
            name=obj.username,
            hash=obj.get_hash(),
            email=obj.email
        )
        # self.add()
        super().create(user_obj)
        return random_id
    
def get_user_service():
    # session = get_session()
    session = create_session()
    return UserService(session)