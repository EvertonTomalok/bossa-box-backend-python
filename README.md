# bossa-box-backend-python

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
- `HEADER`: `token` = `Bearer ...`
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
- `HEADER`: `token` = `Bearer ...`


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
- `HEADER`: `token` = `Bearer ...`
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
- `HEADER`: `token` = `Bearer ...`

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
