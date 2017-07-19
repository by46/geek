import time

from sqlalchemy import event
from sqlalchemy import exc
from sqlalchemy.engine import create_engine
from sqlalchemy.pool import Pool


@event.listens_for(Pool, 'checkout')
def ping_connection(db_api_connection, connection_record, connection_proxy):
    cursor = db_api_connection.cursor()
    try:
        cursor.execute('SELECT 1')
    except:
        raise exc.DisconnectionError()
    cursor.close()


url = "mysql+pymysql://root:root@10.16.76.245:3306/CodeCenter"

engine = create_engine(url, echo=False)
query = 'SELECT NOW()'
while True:
    print('Q1', engine.execute(query).fetchall())
    engine.execute('SET wait_timeout = 2')
    time.sleep(3)
    print("Q2", engine.execute(query).fetchall())
