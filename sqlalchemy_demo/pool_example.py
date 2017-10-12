from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://root:root@10.16.76.245:3306/coffee')
Session = sessionmaker(bind=engine)
session = Session()

session.execute('INSERT demo5(name) VALUES(:Name)', params={'Name': 'Trans1'})
session.execute('INSERT demo5(name) VALUES(:Name)', params={'Name': 'Trans2'})
session.begin_nested()
session.execute('INSERT demo5(name) VALUES(:Name)', params={'Name': 'Trans3'})
session.rollback()
session.begin_nested()
session.execute('INSERT demo5(name) VALUES(:Name)', params={'Name': 'Trans4'})
session.commit()
session.commit()
