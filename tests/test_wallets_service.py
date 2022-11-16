import unittest
from src.services.wallets import get_wallets_service
from src.schema.wallets import NewWallet, Wallet
from typing import Any

class TestWalletsService(unittest.TestCase):
    wallets_service = get_wallets_service()

    def test_create_wallet(self):
        owner_user_id = "IDE5AHA"
        wallet_id = self.wallets_service.create(owner_user_id)
        self.wallets_service.delete(wallet_id)
        self.assertIsNotNone(Wallet)
        self.assertNotEqual(wallet_id, "")
        self.assertNotEqual(wallet_id, " ")
    
    def test_user_unique_wallet(self):
        owner_user_id = "IDE5AHA"
        wallet_id = self.wallets_service.create(owner_user_id)
        with self.assertRaises(Exception) as e:
            self.wallets_service.create(owner_user_id)
        
        self.wallets_service.delete(wallet_id)
    
    def test_get_user_wallet(self,):
        owner_user_id = "IDE5AHA"
        wallet_id = self.wallets_service.create(owner_user_id)
        user_wallet_object: Wallet = self.wallets_service.get_user_wallet(owner_user_id)
        self.wallets_service.delete(wallet_id)
        self.assertEqual(wallet_id, user_wallet_object.id)
