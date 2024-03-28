import pika
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv('HOST')
username = os.getenv('USER')
password = os.getenv('PASSWORD')


def channel(queue):
    print(username, password)
    credentials = pika.PlainCredentials(username=username, password=password)
    connection = pika.BlockingConnection(pika.ConnectionParameters(
        host=host, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue=queue)
    return channel
