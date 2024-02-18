FROM python:3.11.1-slim
LABEL authors="fox"

WORKDIR = /.

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .