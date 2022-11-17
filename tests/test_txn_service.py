import unittest
from src.services.transactions import get_transactions_service
from src.schema.transactions import Transaction, NewTransaction
from tests.testing_config import TestData

class TestTxnService(unittest.TestCase):
    txn_service = get_transactions_service()
    def test_create_txn(self, ):
        new_txn_obj = NewTransaction(
            seller=TestData.wallet_id,
            buyer=TestData.wallet_id,
            bid_id=None
        )
        txn_db_record: Transaction = self.txn_service.create(new_txn_obj)
        self.txn_service.delete(txn_db_record.id)
        self.assertEqual(txn_db_record.buyer, new_txn_obj.buyer)
