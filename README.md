# MVP Terceira Sprint API Usuários

Api que concentra usuários e seus respectivos endereços.

## Tecnologias utiliadas:

- Python
- FastApi
- Graphql
- Postgres
- Docker

## Forma de utilizar

1. Clone o repositório
2. Acesse o diretório do projeto
3. Cire um arquivo .env e insira as variáveis de ambiente abaixo.
   - Por motivos ditádicos esses dados sensivéis (de ambiente local) foram deixados explicitamente na documentação, caso faça em um projeto com dados de produção não os deixe expostos.
```
DB_HOST=users-postgres
DB_PORT=5432
DB_USER=myuser
DB_PASS=mypass
DB_NAME=usersdb
HOST=0.0.0.0
PORT=8001
```
1. Execute o comando
```
docker compose up --build
```

## Exemplos de uso da API GraphQL

Acessar a rota http://localhost:8001/graphql e inserir os payloads abaixo.

#### Criar usuário com endereço

```graphql
mutation {
  createUser(
    nome: "Fulano da Silva"
    email: "fulano@mvp3.com"
    cep: "01001000"
    logradouro: "Praça da Sé"
    bairro: "Sé"
    estado: "SP"
    cidade: "São Paulo"
  ) {
    id
    nome
    email
    address {
      cep
      logradouro
      bairro
      cidade
      estado
    }
  }
}
```

#### Buscar Todos os Usuários

```graphql
query {
  users {
    id
    nome
    email
    address {
      cep
      cidade
      estado
    }
  }
}
```

#### Buscar Usuário por ID

```graphql
query {
  userById(id: 1) {
    id
    nome
    email
    address {
      logradouro
      bairro
      cidade
      estado
    }
  }
}
```

#### Atualizar dados do Usuário

```graphql
mutation {
  updateUser(
    id: 1
    nome: "Fulano Atualizado"
    email: "fulano.novo@example.com"
  ) {
    id
    nome
    email
  }
}
```

#### Excluir Usuário

```graphql
mutation {
  deleteUser(id: 1)
}
```