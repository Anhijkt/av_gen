FROM python:3.6-alpine

WORKDIR /home/prose

RUN apk add build-base
RUN apk add jpeg-dev zlib-dev
RUN apk add linux-headers

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY gen.py gen.py
COPY main.py main.py
COPY boot.sh boot.sh 
EXPOSE 5000

ENTRYPOINT ["./boot.sh"]