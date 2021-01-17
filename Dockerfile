FROM python:3.8

RUN mkdir -p /usr/src/app

ENV TZ=America/Sao_Paulo

WORKDIR /usr/src/app

RUN apt-get update && apt-get install --yes build-essential

RUN pip install pipenv==2018.11.26

ADD Pipfile Pipfile.lock /usr/src/app/

RUN pipenv install --deploy --system

ADD . /usr/src/app/
