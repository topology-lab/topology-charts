FROM python:3.8

# from https://docs.docker.jp/compose/django.html
ENV PYTHONUNBUFFERED 1
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
# <<<<<<<<<<<<<<<<<<<<<<<<<<
# vim
RUN set -x && \
  apt-get update && \
  apt-get install -y vim && \
  pip install --upgrade pip
# >>>>>>>>>>>>>>>>>>>>>>>>>>
RUN pip install -r requirements.txt
ADD . /code/

