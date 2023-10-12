FROM python:3.10

WORKDIR /quiz_service

COPY requirements.txt .

RUN pip install -r requirements.txt --no-cache-dir

COPY . .
