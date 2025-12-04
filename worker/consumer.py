import json
import pika
import os

from service_user import (
    create_user, read_user, update_user, delete_user
)

host = os.getenv("RABBITMQ_HOST", "localhost")

def callback(ch, method, properties, body):
    message = json.loads(body)
    action = message["action"]
    data = message["data"]

    if action == "create_user":
        create_user(data)
    elif action == "read_user":
        read_user(data["id"])
    elif action == "update_user":
        update_user(data)
    elif action == "delete_user":
        delete_user(data["id"])

    print(f"[x] Processado: {message}")

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host)
)
channel = connection.channel()
channel.queue_declare(queue="users_commands")

print("[*] Worker aguardando mensagens...")
channel.basic_consume(
    queue="users_commands",
    on_message_callback=callback,
    auto_ack=True
)

channel.start_consuming()
