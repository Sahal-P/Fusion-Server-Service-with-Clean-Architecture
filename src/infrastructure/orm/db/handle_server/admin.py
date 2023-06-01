from django.contrib import admin

# from src.infrastructure.orm.db.server.consumer import handle_thread

# # Register your models here.
# handle_thread('new-user')
import pika
from .consumer import consumer_thread
# Establish a connection
def produce_messages():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-srv'))  # Replace with your RabbitMQ service name or IP
    
    # Create a channel
    channel = connection.channel()
    
    # Declare a queue
    channel.queue_declare(queue='my_queue')
    
    # Publish a message
    msg= 'Hello, RabbitMQ! this is sahal-------'
    channel.basic_publish(exchange='', routing_key='my_queue', body=msg)
    print('published : ',msg)
    
    # Close the connection
    connection.close()
    
consumer_thread.start()
