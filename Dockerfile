FROM python:3.10-rc-alpine3.12
# MAINTAINER GANGADHAR

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .temp-build-deps \
     gcc libc-dev linux-headers postgresql-dev
RUN pip uninstall psycopg2
RUN pip install --upgrade wheel
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt

RUN apk del .temp-build-deps

RUN mkdir /app
WORKDIR /app
COPY ./app /app

RUN adduser -D gangadhar
USER gangadhar