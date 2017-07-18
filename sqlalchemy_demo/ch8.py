from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import Numeric
from sqlalchemy import String
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:')

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Cookie(Base):
    __tablename__ = 'cookies'
    cookie_id = Column(Integer, primary_key=True)
    cookie_name = Column(String(50), index=True)
    cookie_recipe_url = Column(String(255))
    cookie_sku = Column(String(55))
    quantity = Column(Integer)
    unit_cost = Column(Numeric(12, 2))

    def __init__(self, name, recipe_url=None, sku=None, quantity=0, unit_cost=0.00):
        self.cookie_name = name
        self.cookie_recipe_url = recipe_url
        self.cookie_sku = sku
        self.quantity = quantity
        self.unit_cost = unit_cost

    def __repr__(self):
        return "Cookie(cookie_name='{self.cookie_name}'".format(self=self)


Base.metadata.create_all(engine)
cookie = Cookie('Chaos')
session.add(cookie)
session.commit()
insp = inspect(cookie)
for state in ['transient', 'pending', 'persistent', 'detached']:
    print('{:>10}: {}'.format(state, getattr(insp, state)))
