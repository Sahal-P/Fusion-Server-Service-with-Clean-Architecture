
# Register your models here.
import pika
import concurrent.futures
import threading
import ast
from src.infrastructure.orm.db.handle_user.repositories import UserDataBaseRepository

from src.interface.serializers.account import UserCreatedQueueSerializer

# Establish a connection

def run_rabbitmq_consumer():
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq-srv'))  # Replace with your RabbitMQ service name or IP

    # Create a channel
    channel = connection.channel()

    # Declare a queue
    channel.queue_declare(queue='user-created')

    # Define a callback function for consuming messages
    def process_message(body):
        # Simulate time-consuming processing
        import time
        time.sleep(2)

        # Custom processing logic
        print("Processed message:", body)
        decoded_body = body.decode('utf-8')
        data = ast.literal_eval(decoded_body)
        deserialized_data = UserCreatedQueueSerializer().load(data)
        UserDataBaseRepository().create_user(**deserialized_data)

    # Define a function for processing a single message
    def process_single_message(ch, method, properties, body):
        # Call the message processing function
        process_message(body)

        # Acknowledge the message
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # Set the number of worker threads for parallel processing
    num_worker_threads = 4

    # Create a thread pool executor
    executor = concurrent.futures.ThreadPoolExecutor(max_workers=num_worker_threads)

    # Start consuming messages
    channel.basic_qos(prefetch_count=num_worker_threads)
    channel.basic_consume(queue='user-created', on_message_callback=process_single_message)

    # Enter a never-ending loop to continuously consume messages
    try:
        print('Consuming messages...')
        with executor:
            channel.start_consuming()
    except KeyboardInterrupt:
        # Gracefully close the connection if interrupted by the user
        connection.close()

    
consumer_thread = threading.Thread(target=run_rabbitmq_consumer)

# Start the consumer thread