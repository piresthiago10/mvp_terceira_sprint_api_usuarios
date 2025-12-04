from models import User
from db import SessionLocal

def create_user(data):
    db = SessionLocal()
    print("Data:", data)
    user = User(**data)
    db.add(user)
    db.commit()
    db.close()

def read_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    db.close()
    if user:
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email
        }

def update_user(data):
    db = SessionLocal()
    user = db.query(User).filter(User.id == data["id"]).first()
    if user:
        user.username = data.get("username", user.username)
        user.email = data.get("email", user.email)
        db.commit()
    db.close()

def delete_user(user_id):
    db = SessionLocal()
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    db.close()
