from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False, index=True)

    address = relationship("Address", back_populates="user", uselist=False)


class Address(Base):
    __tablename__ = "addresses"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)

    cep = Column(String, nullable=False)
    logradouro = Column(String, nullable=False)
    bairro = Column(String, nullable=False)
    estado = Column(String, nullable=False)
    cidade = Column(String, nullable=False)

    user = relationship("User", back_populates="address")
