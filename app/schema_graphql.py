import strawberry
import strawberry
from typing import Optional, List
from .models import User as UserModel, Address as AddressModel
from .database import SessionLocal


@strawberry.type
class Address:
    cep: str
    logradouro: str
    bairro: str
    estado: str
    cidade: str


@strawberry.type
class User:
    id: int
    nome: str
    email: str
    address: Optional[Address]

@strawberry.type
class PaginatedUsers:
    items: List[User]
    page: int
    per_page: int
    total: int
    total_pages: int


def address_to_graphql(model: AddressModel) -> Address:
    return Address(
        cep=model.cep,
        logradouro=model.logradouro,
        bairro=model.bairro,
        estado=model.estado,
        cidade=model.cidade,
    )


def user_to_graphql(model: UserModel) -> User:
    return User(
        id=model.id,
        nome=model.nome,
        email=model.email,
        address=address_to_graphql(model.address) if model.address else None
    )

@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        db = SessionLocal()
        try:
            data = db.query(UserModel).all()
            return [user_to_graphql(u) for u in data]
        finally:
            db.close()

    @strawberry.field
    def user_by_id(self, id: int) -> Optional[User]:
        db = SessionLocal()
        try:
            item = db.query(UserModel).filter(UserModel.id == id).first()
            return user_to_graphql(item) if item else None
        finally:
            db.close()

    @strawberry.field
    def users_paginated(
        self,
        page: int = 1,
        per_page: int = 10
    ) -> PaginatedUsers:

        db = SessionLocal()
        try:
            total = db.query(UserModel).count()
            total_pages = (total + per_page - 1) // per_page
            offset = (page - 1) * per_page

            items_db = (
                db.query(UserModel)
                .offset(offset)
                .limit(per_page)
                .all()
            )

            items = [user_to_graphql(u) for u in items_db]

            return PaginatedUsers(
                items=items,
                page=page,
                per_page=per_page,
                total=total,
                total_pages=total_pages
            )
        finally:
            db.close()

@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(
        self,
        nome: str,
        email: str,
        cep: str,
        logradouro: str,
        bairro: str,
        estado: str,
        cidade: str
    ) -> User:

        db = SessionLocal()
        try:
            user = UserModel(nome=nome, email=email)
            db.add(user)
            db.commit()
            db.refresh(user)

            address = AddressModel(
                user_id=user.id,
                cep=cep,
                logradouro=logradouro,
                bairro=bairro,
                estado=estado,
                cidade=cidade
            )
            db.add(address)
            db.commit()
            db.refresh(address)

            return user_to_graphql(user)
        finally:
            db.close()


schema = strawberry.Schema(query=Query, mutation=Mutation)
