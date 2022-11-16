import unittest
from src.services.bids import get_bids_service
from src.schema.bids import AddNewBid, BidStatus
from random import randint

class TestBidsService(unittest.TestCase):
    bids_service = get_bids_service()
    def test_create_bid(self,):
        create_bid_obj = AddNewBid(
            asset_id="GRTLYZZ",
            bidder="IDE5AHA",
            quote_price=250000
        )
        id = self.bids_service.create(create_bid_obj)
        bid_db_obj = self.bids_service.get(id)
        self.assertEqual(id, bid_db_obj.id)
        self.bids_service.delete(id)
    
    def test_multiple_bids(self,):
        asset_id="GRTLYZZ"
        bidder="IDE5AHA"
        quote_price = 250000
        ids = []
        for _ in range(0, 100):
            quote_price += 100
            bid_obj = AddNewBid(
                bidder=bidder,
                asset_id=asset_id,
                quote_price=quote_price
            )
            ids.append(self.bids_service.create(bid_obj))
        
        bids = self.bids_service.list_bids_for_an_asset(asset_id)
        self.assertEqual(len(bids), len(ids))
        for bid_id in ids:
            self.bids_service.delete(bid_id)


    def test_get_max_bid(self,):
        asset_id="GRTLYZZ"
        bidder="IDE5AHA"
        # quote_price = 250000
        ids = []
        bid_quotes = []
        quote_price = 250000
        for _ in range(0, 100):
            quote_price +=randint(100, 500)
            # quote_price+=5000
            bid_obj = AddNewBid(
                bidder=bidder,
                asset_id=asset_id,
                quote_price=quote_price
            )
            ids.append(self.bids_service.create(bid_obj))
            bid_quotes.append(quote_price)
        
        # bids = self.bids_service.list_bids_for_an_asset(asset_id)
        max_bid = self.bids_service.get_highest_bid_for_an_asset(asset_id)
        self.assertEqual(max_bid, max(bid_quotes))
        # self.assertEqual(len(bids), len(ids))
        for bid_id in ids:
            self.bids_service.delete(bid_id)
        return
    
