from sqlalchemy import *
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import *
import os

Base = declarative_base()

DB_URL = 'postgresql://orders:0rd3rs@localhost:5432/orders'

if 'DB_URL' in os.environ:
    DB_URL = os.environ['DB_URL']

engine = create_engine(DB_URL)
session = sessionmaker()
session.configure(bind=engine)
Base.metadata.create_all(engine)


class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    name = Column(String)


class OrderRepository(object):

    def delete_all(self):
        # Order.query().delete()
        rows_deleted = self.session.query(Order).delete()
        return rows_deleted

    def __init__(self):
        self.session = session()

    def all(self):
        return self.session.query(Order).all()

    def by_id(self, id):
        return self.session.query(Order, id=id).all()

    def insert(self, name=''):
        order = Order(name="Kimly")
        self.session.add(order)
        self.session.commit()
        return order

    def count(self):
        return self.session.query(Order).count()
