FROM python:3.10.5-buster

RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install binutils libproj-dev apt-transport-https ca-certificates

ENV PYTHONUNBUFFERED 1
RUN pip3 install pipenv

COPY Pipfile .
COPY Pipfile.lock .

RUN pipenv requirements --dev > requirements.txt
RUN pip install -r requirements.txt
COPY . /app
WORKDIR /app
