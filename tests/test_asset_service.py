import unittest
from psycopg2.errors import ForeignKeyViolation, IntegrityError
from src.schema.assets import AddAsset
from src.services.assets import get_assets_service

class TestAssetService(unittest.TestCase):
    assets_service = get_assets_service()

    def test_add_asset(self, ):
        add_asset_obj = AddAsset(
            description="My spotify playlist with a gazillion listeners",
            price=2000*100,
            for_sale=True,
            asset_url="https://open.spotify.com/playlist/401EoOfjzh4YhPcmsXdPq9?si=bda5ab15b8a44824",
            owner="IDE5AHA"
        )
        id = self.assets_service.create(add_asset_obj)
        db_asset_obj = self.assets_service.get(id)
        self.assertEqual(add_asset_obj.asset_url, db_asset_obj.asset_url)
        self.assertEqual(add_asset_obj.price, db_asset_obj.price)
    
    def test_add_asset_invalid_owner(self,):
        add_asset_obj = AddAsset(
            description="My spotify playlist with a gazillion listeners",
            price=2000*100,
            for_sale=True,
            asset_url="https://open.spotify.com/playlist/401EoOfjzh4YhPcmsXdPq9?si=bda5ab15b8a44824",
            owner="invalid_user_id"
        )
        with self.assertRaises(Exception) as e:
            id = self.assets_service.create(add_asset_obj)
        self.assertTrue(isinstance(e.exception.orig, ForeignKeyViolation))
