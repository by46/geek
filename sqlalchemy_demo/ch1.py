from sqlalchemy import Column, Integer, String
from sqlalchemy import ForeignKey
from sqlalchemy import MetaData
from sqlalchemy import create_engine
from sqlalchemy import func
from sqlalchemy import text
from sqlalchemy.ext.declarative import DeclarativeMeta
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import aliased
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import exists

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()  # type: DeclarativeMeta


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)

    def __repr__(self):
        return "<User(Id={3}, name='{0}', fullname='{1}', password='{2}'>".format(
            self.name, self.fullname, self.password, self.id)


class Address(Base):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    email_address = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='addresses')

    def __repr__(self):
        return '<Address(Id={0}, email={1}>'.format(self.id, self.email_address)


class Book(Base):
    __tablename__ = 'books'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    user_id = Column(Integer)
    user = relationship('User', primaryjoin=user_id == User.id,
                        back_populates='books',
                        foreign_keys=user_id,
                        remote_side=User.id)

    def __repr__(self):
        return '<Book(Id={0}, name={1}>'.format(self.id, self.name)


User.addresses = relationship('Address', order_by=Address.id, back_populates='user')

User.books = relationship('Book', back_populates='user',
                          primaryjoin=User.id == Book.user_id,
                          foreign_keys=Book.user_id,
                          remote_side=User.id)

user_alias = aliased(User, name='user_alias')

metadata = Base.metadata  # type: MetaData
metadata.create_all(engine)

user = User(name='benjamin', fullname='benjamin.c.yan', password='123456')
session = Session()
session.add(user)
new_user = session.query(User).filter_by(name='benjamin').first()  # type: User
print(new_user, new_user.addresses)
session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')])

new_user.name = 'wendy'
print (session.dirty)
session.commit()

for user in session.query(User).order_by(User.id.desc()):
    print(user.name, user.fullname)

for name, fullname in session.query(User.name, User.fullname).filter(User.id > 2).filter(User.name == 'mary'):
    print(name, fullname)

for row in session.query(User.name, User.fullname):
    print(row.name, row.fullname)

for row in session.query(User.name.label('name_label')).all():
    print(row.name_label)

for row in session.query(user_alias, user_alias.name).all():
    print(row.user_alias)

for row in session.query(User).order_by(User.id)[1:3]:
    print(row)

session.query(User).filter(User.name.in_(['wendy'])).all()
session.query(User).filter(~User.name.in_(['wendy'])).all()
session.query(User).filter(User.name.isnot(None)).all()
print(session.query(User).from_statement(text('SELECT * FROM users where name=:name')
                                         ).params(name='wendy').all())

session.query(User).count()
session.query(func.count(User.name)).filter(User.name == 'wendy').all()
print(session.query(func.count(User.name), User.name).group_by(User.name).all())
print(session.query(func.count('1')).select_from(User).scalar())
session.query(func.count(User.id)).scalar()

new_user.addresses = [
    Address(email_address='benjamin.c.yan@newegg.com'),
    Address(email_address='benjamin.c.yan2@newegg.com')
]

session.commit()
print(new_user.addresses)
print(new_user.addresses[1].user)

book = Book(name='Programming the 80386')
book.user = new_user
session.add(book)
session.commit()
print(book.user, book.user.books)

print('----------------------------------separate-----------------------')
for book in list(new_user.books):
    new_user.books.remove(book)
session.commit()
new_user.books.append(book)
new_user.books.append(Book(name='Programming the 803862'))
session.commit()

stmt = session.query(Address.user_id, func.count(Address.user_id).label('address_count')
                     ).group_by(Address.user_id).subquery()

for u, count in session.query(User, stmt.c.address_count).outerjoin(stmt, User.id == stmt.c.user_id
                                                                    ).order_by(User.id):
    print(u, count)

print ('----------------------------separate2-----------------------')
stmt = session.query(Address).filter(Address.email_address != 'benjamin').subquery()

address_alias = aliased(Address, stmt)
for user, address in session.query(User, address_alias).join(address_alias, User.addresses):
    print(user, address)

print('------------------------------separate3-----------------------------')
stmt = exists().where(Address.user_id == User.id)
for name, in session.query(User.name).filter(stmt):
    print(name)
