from sqlalchemy import Boolean, Column, Enum, Float, ForeignKey, Integer, String, TIMESTAMP, null, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from src.schema.bids import BidStatus
Base = declarative_base()


class Users(Base):
    __tablename__ = 'users'
    id = Column(String, primary_key=True)
    name = Column(String) 
    email = Column(String)
    verified = Column(Boolean)
    hash = Column(String)
    __table_args__ = (UniqueConstraint("email", "name", name="email_name_unq"), )

class Assets(Base):
    __tablename__ = 'assets'
    id = Column(String, primary_key=True)
    description = Column(String, default="")
    owner = Column(String, ForeignKey("users.id"), nullable=False)
    price = Column(Integer, nullable=False)
    for_sale = Column(Boolean, default=True)
    asset_url = Column(String, default="")
    timestamp = Column(TIMESTAMP(timezone=False), nullable=False, default=datetime.utcnow())


class Transactions(Base):
    # If entry is true then this is a entry_transaction and ts is the same as
    # tsRead
    __tablename__ = 'transactions'
    id = Column(String, primary_key=True)
    seller = Column(String, ForeignKey("wallets.id"), nullable=False)
    buyer = Column(String, ForeignKey("wallets.id"), nullable=False)
    bid_id = Column(String, ForeignKey("bids.id"), nullable=True)
    timestamp = Column(TIMESTAMP)
    ref_url = Column(String, default="")
    note = Column(String, default="")


class Bids(Base):   
    ## TODO: Add back status of the bids and see how we can make it enums
    __tablename__ = "bids"
    id = Column(String, primary_key=True)
    bidder = Column(String, ForeignKey("users.id"), nullable=False)
    # txn_id = Column(String, ForeignKey("transactions.id"), nullable=False)
    asset_id = Column(String, ForeignKey("assets.id"), nullable=False)
    quote_price = Column(Integer, nullable=False)
    # status = Column(Enum("placed"))
    status = Column(String, nullable=False, default="placed")
    timestamp = Column(TIMESTAMP)

class Wallets(Base):
    __tablename__ = "wallets"
    id = Column(String, primary_key=True)
    owner = Column(String, ForeignKey("users.id"), nullable=False)
    balance = Column(Integer, default=0)
    escrow_balance = Column(Integer, default=0)
    last_updated = Column(TIMESTAMP)

    __table_args__ = (UniqueConstraint("owner"), )
