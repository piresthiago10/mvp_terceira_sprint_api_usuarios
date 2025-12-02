import pika
import os

class RabbitMQService:
    def __init__(self):
        url = os.getenv("RABBITMQ_URL")
        params = pika.URLParameters(url)
        self.connection = pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="user_events", durable=True)

    def publish(self, event: dict):
        self.channel.basic_publish(
            exchange="",
            routing_key="user_events",
            body=str(event).encode(),
            properties=pika.BasicProperties(delivery_mode=2)
        )
