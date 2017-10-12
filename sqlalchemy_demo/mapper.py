from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import inspect
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import Mapper
from sqlalchemy.orm import mapper
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)

metadata = MetaData()

user = Table('user', metadata,
             Column('id', Integer, primary_key=True),
             Column('name', String(50)),
             Column('fullname', String(50)),
             Column('password', String(12)))


class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password


address = Table('address', metadata,
                Column('id', Integer, primary_key=True),
                Column('user_id', Integer, ForeignKey('user.id')),
                Column('email_address', String(50)))


class Address(object):
    def __init__(self, email_address):
        self.email_address = email_address


mapper(User, user, properties={
    'addresses': relationship(Address, backref='user', order_by=address.c.id)
})
mapper(Address, address)

insp = inspect(User)  # type: Mapper
print(insp, insp.columns)
print(list(insp.columns))
