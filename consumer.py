import pika
import sys
import os
from config import channel

queue = channel('hello')

def callback(ch, method, properties, body):
    print(f" [x] Received {body}")
    queue.basic_ack(delivery_tag = method.delivery_tag)

def main():
    queue.basic_consume(queue='hello', on_message_callback=callback, auto_ack=False)
    queue.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)