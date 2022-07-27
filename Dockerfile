FROM python:3.6

ENV PYTHONUNBUFFERED 1

RUN mkdir /libraryapi

WORKDIR /libraryapi

ADD . /libraryapi/

RUN pip install -r requirements.txt