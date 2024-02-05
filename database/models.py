from sqlalchemy import Column, String, Integer, DateTime, Date, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    surname = Column(String)
    phone_number = Column(Integer, unique=True)
    email = Column(String)
    city = Column(String)
    password = Column(String)
    reg_date = Column(DateTime)


class UserCard(Base):
    __tablename__ = 'cards'
    card_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey('users.user_id'))
    card_number = Column(Integer, nullable=False, unique=True)
    balance = Column(Float, default=0)
    exp_date = Column(Integer)
    card_name = Column(String)

    user_fk = relationship(User, lazy='subquery')


class Transfer(Base):
    __tablename__ = 'transfers'
    transfer_id = Column(Integer, primary_key=True, autoincrement=True)
    card_from_id = Column(Integer, ForeignKey('cards_card_id'))
    card_to_id = Column(Integer, ForeignKey('card_card_id'))
    amount = Column(Float)

    status = Column(Boolean, default=True)

    transaction_date = Column(DateTime)

    card_from_fk = relationship(UserCard, lazy='subquery')
    card_to_fk = relationship(UserCard, lazy='subquery')
