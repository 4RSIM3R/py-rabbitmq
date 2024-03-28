
import pika
from config import channel

queue = channel('hello')

queue.basic_publish(exchange='',
                    routing_key='hello',
                    body='New Line Not Disappear because auto ack',
                    properties=pika.BasicProperties(
                        delivery_mode=pika.DeliveryMode.Persistent
                    ))
