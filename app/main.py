from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from .database import Base, engine
from .schema_graphql import schema


# cria tabelas
Base.metadata.create_all(bind=engine)


app = FastAPI(title="Users API - GraphQL")


gql = GraphQLRouter(schema)
app.include_router(gql, prefix="/graphql")


@app.get("/")
def root():
    return {"msg": "Users API - use /graphql"}