import uvicorn
from fastapi import FastAPI
from .routers.users import router as users_router
import os

app = FastAPI()
app.include_router(users_router)

print("Rabbit:", ">"*200, os.getenv("RABBITMQ_HOST"))
print("DB:", ">"*200, os.getenv("DATABASE_URL"))