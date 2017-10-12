from sqlalchemy import Column
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import MetaData
from sqlalchemy import String
from sqlalchemy import Table
from sqlalchemy import Text
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column_property
from sqlalchemy.orm import relationship
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
Base = declarative_base()

post_keywords = Table('post_keywords', Base.metadata,
                      Column('post_id', ForeignKey('posts.id'), primary_key=True),
                      Column('keyword_id', ForeignKey('keywords.id'), primary_key=True))


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    password = Column(String)
    title = column_property(name + ' ' + fullname)

    def __repr__(self):
        return "<User(Id={3}, name='{0}', fullname='{1}', password='{2}', title={3}>".format(
            self.name, self.fullname, self.password, self.id, self.title)


class BlogPost(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    headline = Column(String(255), nullable=False)
    body = Column(Text)

    keywords = relationship('Keyword', secondary=post_keywords,
                            back_populates='posts')

    def __repr__(self):
        return '<BlogPost(Id={0}, author={1}, headline={2}>'.format(
            self.id, self.author, self.headline)


class Keyword(Base):
    __tablename__ = 'keywords'
    id = Column(Integer, primary_key=True)
    keyword = Column(String(50), nullable=False, unique=True)
    posts = relationship('BlogPost', secondary=post_keywords,
                         back_populates='keywords')


BlogPost.author = relationship(User, back_populates='posts')
User.posts = relationship(BlogPost, back_populates='author', lazy='dynamic')

metadata = Base.metadata  # type: MetaData
metadata.create_all(engine)
session = Session()

session.add_all([
    User(name='wendy', fullname='Wendy Williams', password='foobar'),
    User(name='mary', fullname='Mary Contrary', password='xxg527'),
    User(name='fred', fullname='Fred Flinstone', password='blah')])

wendy = session.query(User).filter_by(name='wendy').one()
post = BlogPost(headline="Wendy's Blog post", body="Blog", author=wendy)
session.add(post)

post.keywords.append(Keyword(keyword='Wendy'))
post.keywords.append(Keyword(keyword='FirstPost'))
session.commit()

print(session.query(BlogPost).filter(BlogPost.keywords.any(keyword='FirstPost')).all())
