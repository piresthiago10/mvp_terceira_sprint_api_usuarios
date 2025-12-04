from fastapi import APIRouter
from ..rabbitmq import RabbitMQService

router = APIRouter(prefix="/users")

@router.post("/")
def create_user(user: dict):
    RabbitMQService().send("create_user", user)
    return {"status": "sent", "action": "create_user"}

@router.get("/{user_id}")
def read_user(user_id: int):
    result = RabbitMQService().send("read_user", {"id": user_id})
    return {
        "status": "sent",
        "action": "read_user",
        "result": result
        }

@router.put("/{user_id}")
def update_user(user_id: int, user: dict):
    data = {"id": user_id, **user}
    RabbitMQService().send("update_user", data)
    return {"status": "sent"}

@router.delete("/{user_id}")
def delete_user(user_id: int):
    RabbitMQService().send("delete_user", {"id": user_id})
    return {"status": "sent"}
