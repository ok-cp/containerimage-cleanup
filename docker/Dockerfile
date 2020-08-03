FROM python:3.8.5-alpine3.11
MAINTAINER ok-cp

RUN apk add docker
RUN pip3 install --upgrade pip

ADD cleanup.sh /
ADD main.py /
WORKDIR /

RUN chmod 755 main.py cleanup.sh
