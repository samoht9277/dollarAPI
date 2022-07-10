FROM python:latest

WORKDIR /docker

COPY . /docker

RUN apt-get update && apt-get install -y python3-pip

RUN pip install -r requirements.txt

CMD gunicorn -c gunicorn.conf.py app:app