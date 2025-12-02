from fastapi import FastAPI
from .database import Base, engine
from .routers import users

# Cria tabelas automaticamente
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Users API MVP Sprint 3",
    version="1.0.0"
)

app.include_router(users.router)

@app.get("/")
def root():
    return {"msg": "Users API is running!"}
