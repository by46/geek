from pika import BasicProperties
from pika import BlockingConnection
from pika import ConnectionParameters


def producer():
    connection = BlockingConnection(ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='logs',
                             type='fanout')

    message = "info: Hello World!"

    channel.basic_publish(
        exchange='exchange_delay_begin',
        routing_key='delay',
        body=message,
        properties=BasicProperties(
            delivery_mode=2,  # make message persistent
            expiration="6000"
        )
    )
    print(" [x] Sent %r" % message)

    connection.close()


def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)


def consumer():
    conn = BlockingConnection(ConnectionParameters('localhost'))
    channel = conn.channel()
    channel.basic_consume(callback,
                          queue='queue_delay_done',
                          no_ack=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    producer()
    consumer()
