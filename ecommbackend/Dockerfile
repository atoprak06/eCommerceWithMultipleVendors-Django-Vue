FROM python:alpine3.16
WORKDIR /opt/ecomm-backend
COPY . .
RUN apk update
RUN apk add postgresql-dev gcc python3-dev musl-dev
RUN ["pip","install","-r","requirements.txt"]
RUN ["pip","install","psycopg2"]
EXPOSE 8000

