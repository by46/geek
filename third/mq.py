from pika import BlockingConnection
from pika import ConnectionParameters


def producer():
    connection = BlockingConnection(ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                             type='fanout')

    message = "info: Hello World!"
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=message)
    print(" [x] Sent %r" % message)
    connection.close()


def consumer():
    conn = BlockingConnection(ConnectionParameters('localhost'))
    channel = conn.channel()
    channel.exchange_declare(exchange='logs',
                             type='fanout')
    result = channel.queue_declare(exclusive=True)
    queue_name = result.method.queue

    channel.queue_bind(exchange='logs',
                       queue=queue_name)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(" [x] %r" % body)

    channel.basic_consume(callback,
                          queue=queue_name,
                          no_ack=True)

    channel.start_consuming()


if __name__ == '__main__':
    producer()
    consumer()