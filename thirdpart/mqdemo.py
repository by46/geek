import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
# channel.queue_declare(queue='dfis2')

channel.basic_publish(exchange='',
                      routing_key='dfis',
                      body='Hello World!')
print(" [x] Sent 'Hello World!'")