from pika import BlockingConnection
from pika import ConnectionParameters

if __name__ == '__main__':
    conn = BlockingConnection(ConnectionParameters('localhost'))
    channel = conn.channel()
    channel.basic_publish(exchange='',
                          routing_key='benjamin',
                          body='hello world')
    print 'producer'
    channel.close()
