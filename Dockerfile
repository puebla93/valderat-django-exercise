FROM python:3.10

ENV PYTHONUNBUFFERED 1

RUN set -ex \
    && apt-get update \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /api
COPY . .
RUN pip install -r requirements.txt
