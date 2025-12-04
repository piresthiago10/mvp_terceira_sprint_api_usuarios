import json
import pika
import os

class RabbitMQService:
    def __init__(self):
        host = os.getenv("RABBITMQ_HOST", "rabbit")
        self.connection = pika.BlockingConnection(
            pika.ConnectionParameters(host)
        )
        self.channel = self.connection.channel()
        self.channel.queue_declare(queue="users_commands")

    def send(self, action: str, data: dict):
        message = {"action": action, "data": data}
        self.channel.basic_publish(
            exchange="",
            routing_key="users_commands",
            body=json.dumps(message)
        )
        return message
