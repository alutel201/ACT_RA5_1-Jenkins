FROM python:3.10-slim

WORKDIR /app

COPY ./python ./python

WORKDIR /app/python

CMD ["python3", "calculadora.py"]
