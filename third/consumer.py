from pika import BlockingConnection
from pika import ConnectionParameters


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


if __name__ == '__main__':
    conn = BlockingConnection(ConnectionParameters('localhost'))
    channel = conn.channel()
    channel.queue_declare(queue='benjamin')
    channel.basic_consume(callback,
                          queue='benjamin',
                          no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
