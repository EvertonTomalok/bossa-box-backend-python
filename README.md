# bossa-box-backend-python

This ReadMe has two version. One in english, and another in Portuguese.

- [English Version](#english-version)
- [Versão em Português](#versao-em-portugues)

# English Version

A Python API REST, that implements CRUD in a MongoDB database.

# Description

This program has a Makefile with some receipts to help us developing/deploying.

## Setup

Open a terminal in project root, and type:

    - make setup

## Creating the container and running it

In the same terminal, type:

    - make up

## Starting the Web Server

After a quickly period of time (about 30 seconds), type in the same terminal:

    - make web

## Simulating a Web Crawler

For each document added by the endpoint, a message is sent to a Kafka topic (with the name `SCRAPPING_TOPIC`), 
which the worker will read this topic to realize some actions with it.

Open a new terminal, in the project root, and type:

    - make start-kafka-scrapping-worker

## Checking the system
Curl this endpoint below to check if it's healthy, typing:

```
curl --request GET 'http://127.0.0.1:3000/health'
```

It must return "ok"


# ENDPOINTS

## Docs
To see the documentation about available endpoints, use:

- `METHOD`: `GET`
- `ENDPOINT`: /docs

## Generate a token

Generate a new token to use in the ENDPOINT below ( it has a 1-hour duration ):

- `METHOD`: `POST`
- `ENDPOINT`: /token
- `BODY`:
```
{
     "user": "Some User"
}
```

 `RETURNS`:

```
{
    "status": "ok",
    "data": {
        "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiRXZlcnRvbiBUb21hbG9rIiwiZXhwIjoxNjEwOTAxMzgxfQ.kWluJ6MDoCGJBdMcT9DlI75ZabER32g43VWT4EO45LQ"
    }
}
```


## Adding new document

- `METHOD`: `POST`
- `ENDPOINT`: /tools
- `HEADER`: `authorization` = `Bearer ...`
- `BODY`:
```
{
     "title": "Api",
     "link": "https://github.com/python/node-scrapper",
     "description": "Webservice.",
     "tags":["node", "express",  "scrapping", "axios"]
 }
```

 `RETURNS`:

```
{
    "status": "ok",
    "data": {
        "title": "Api",
        "link": "https://github.com/python/node-scrapper",
        "description": "Webservice.",
        "tags": [
            "node",
            "express",
            "scrapping",
            "axios"
        ],
        "id": "SOME ID"
    }
}
```


## Searching for Documents

This endpoint will search for documents. If you only call it, it'll return all the documents.

You could use parameters, as `tag` to filter results by tag, and `skip` to set an offset, and `limit` to limit the number of returning documents.

- `METHOD`: `GET`
- `ENDPOINT`: /tools
- `PARAMETROS`: OPTIONAL
  - tag (set a filter by tag)
  - skip (skip documents)
  - limit  (limit documents)
- `HEADER`: `authorization` = `Bearer ...`


 `RETORNO`:

```
{
    "status": "ok",
    "data": [
        {
            "title": "Api",
            "link": "https://github.com/python/node-scrapper",
            "description": "Webservice.",
            "tags": [
                "node",
                "express",
                "scrapping",
                "axios"
            ],
            "id": "SOME ID"
        },
        {
            "title": "WebServer",
            "link": "https://github.com/python/node-webserver",
            "description": "Web",
            "tags": [
                "node",
                "express",
                "react",
                "mongodb"
            ],
            "id": "SOME ID"
        },
        ...
    ]
}
```

## Editing document

Endpoint to edit a document

- `METHOD`: `PUT`
- `ENDPOINT`: /tools/:id
- `HEADER`: `authorization` = `Bearer ...`
- `BODY`:
```
{
     "title": "New API",
     "link": "https://github.com/python/python-new-api",
     "description": "NEW Webservice.",
     "tags":["python", "requests",  "scrapping", "bs4", "xpath"]
 }
```

 `RETURNS`:

```
{
    "status": "ok",
    "data": {
        "title": "New API",
        "link": "https://github.com/python/python-new-api",
         "description": "NEW Webservice.",
         "tags":["python", "requests",  "scrapping", "bs4", "xpath"]
         "id": "SOME ID"
    }
}
```

## Removing a document

Endpoint to remove a document by IDs

- `METHOD`: `DELETE`
- `ENDPOINT`: /tools/:id
- `HEADER`: `authorization` = `Bearer ...`

 `RETORNO`:

```
    204 NO CONTENT
```

# Environment variables


| Key                              | Description                                      |
|----------------------------------|--------------------------------------------------|
| MONGO_URL                        | Database's URL                                   |
| JWT_SECRET                       | JWT secret generation                            |
| TIME_TO_TOKEN_EXPIRES_IN_MINUTES | Time to expire the JWT                           |
| KAFKA_BROKER                     | Kafka broker's URL                               |


--------------------------------

# Versão em Português

API REST, utilizando BACKEND em python, que realiza CRUD de tools em um banco de dados NoSQL (MongoDB).

# Preparando o ambiente

Este código, possui um arquivo Makefile com diversas receitas, para auxiliar no desenvolvimento/deploy
do código.

## Setup

Abra um terminal, no root do projeto, e digite:

    - make setup

## Subindo os requerimentos necessários

No mesmo terminal, digite:

    - make up

## Subindo o ambiente web

Após um curto periodo de tempo (cerca de 30 segundos), digite no mesmo terminal:

    - make web

## Iniciando o worker para simular scrapping dos links adicionados em cada documento

Para cada documento adicionado pelo endpoint, uma mensagem é enviada para o tópico kafka de nome
SCRAPPING_TOPIC, o qual temos um worker especifico para ler esse tópico e realizar certas ações com
a mensagem.

Abra um novo terminal no root do projeto, e digite:

    - make start-kafka-scrapping-worker


## Verificando o ambiente

Utilize o curl para verificar se o sistema esta funcinando corretamente, digitando:

```
curl --request GET 'http://127.0.0.1:3000/health'
```

Deve retornar "ok"


# ENDPOINTS

## Docs
Para ver a documentação em swagger:

- `METHOD`: `GET`
- `ENDPOINT`: /docs

## Gerar token

Gere um novo token para utilizar nos ENDPOINTS abaixo ( o token tem  DURAÇÃO DE 1 HORA ):

- `METHOD`: `POST`
- `ENDPOINT`: /token
- `BODY`:
```
{
     "user": "Some User"
}
```

 `RETORNO`:

```
{
    "status": "ok",
    "data": {
        "token": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyIjoiRXZlcnRvbiBUb21hbG9rIiwiZXhwIjoxNjEwOTAxMzgxfQ.kWluJ6MDoCGJBdMcT9DlI75ZabER32g43VWT4EO45LQ"
    }
}
```


## Adicionar novo documento

- `METHOD`: `POST`
- `ENDPOINT`: /tools
- `HEADER`: `authorization` = `Bearer ...`
- `BODY`:
```
{
     "title": "Api",
     "link": "https://github.com/python/node-scrapper",
     "description": "Webservice.",
     "tags":["node", "express",  "scrapping", "axios"]
 }
```

 `RETORNO`:

```
{
    "status": "ok",
    "data": {
        "title": "Api",
        "link": "https://github.com/python/node-scrapper",
        "description": "Webservice.",
        "tags": [
            "node",
            "express",
            "scrapping",
            "axios"
        ],
        "id": "SOME ID"
    }
}
```


## Procurar Documentos

Rota para procurar documentos. Caso apenas chamada, trás todos os documentos ( lógica de negócio ).
Aceita parametros `tag` para filtro, e `skip` para pular documentos, e `limit` para limitar numero de documentos
no retorno.

- `METHOD`: `GET`
- `ENDPOINT`: /tools
- `PARAMETROS`: OPCIONAIS
  - tag (filtrar pela tag)
  - skip (pula numero de documentos)
  - limit  (limita o numero de documentos)
- `HEADER`: `authorization` = `Bearer ...`


 `RETORNO`:

```
{
    "status": "ok",
    "data": [
        {
            "title": "Api",
            "link": "https://github.com/python/node-scrapper",
            "description": "Webservice.",
            "tags": [
                "node",
                "express",
                "scrapping",
                "axios"
            ],
            "id": "SOME ID"
        },
        {
            "title": "WebServer",
            "link": "https://github.com/python/node-webserver",
            "description": "Web",
            "tags": [
                "node",
                "express",
                "react",
                "mongodb"
            ],
            "id": "SOME ID"
        },
        ...
    ]
}
```

## Editar documento

Rota para edição de documento

- `METHOD`: `PUT`
- `ENDPOINT`: /tools/:id
- `HEADER`: `authorization` = `Bearer ...`
- `BODY`:
```
{
     "title": "New API",
     "link": "https://github.com/python/python-new-api",
     "description": "NEW Webservice.",
     "tags":["python", "requests",  "scrapping", "bs4", "xpath"]
 }
```

 `RETORNO`:

```
{
    "status": "ok",
    "data": {
        "title": "New API",
        "link": "https://github.com/python/python-new-api",
         "description": "NEW Webservice.",
         "tags":["python", "requests",  "scrapping", "bs4", "xpath"]
         "id": "SOME ID"
    }
}
```

## Remover documento

Rota para remoção de documento por um ids

- `METHOD`: `DELETE`
- `ENDPOINT`: /tools/:id
- `HEADER`: `authorization` = `Bearer ...`

 `RETORNO`:

```
    204 NO CONTENT
```

# Variáveis de ambiente


| Chave                            | Descrição                                        |
|----------------------------------|--------------------------------------------------|
| MONGO_URL                        | URL de acesso ao banco                           |
| JWT_SECRET                       | Segredo para geração de token                    |
| TIME_TO_TOKEN_EXPIRES_IN_MINUTES | Tempo de expiração em minutos de um token gerado |
| KAFKA_BROKER                     | URL de acesso ao broker do kafka                 |
