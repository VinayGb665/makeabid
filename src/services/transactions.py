from src.db.models import Transactions
from sqlalchemy.orm import Session
from src.db.session import create_session
from src.schema.transactions import Transaction, NewTransaction
from src.services.base import BaseService
from typing import Any

class TransactionsService(BaseService[Transactions, Any, Any]):
    def __init__(self, db_session: Session):
        super().__init__(Transactions, db_session)
    
    def create(self, obj: NewTransaction) -> Transaction:
        id = self.generate_id()
        txn_obj = Transaction(
            id=id,
            **obj.dict()
        )
        txn_db_record: Transactions = super().create(txn_obj)
        return Transaction.from_orm(txn_db_record)
    
def get_transactions_service():
    session = create_session()
    return TransactionsService(session)