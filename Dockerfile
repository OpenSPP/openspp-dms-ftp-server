FROM python:3.10-slim-bullseye

RUN apt update -y && apt install openssl

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir -p /etc/ssl/certs/openspp &&  \
    cd /etc/ssl/certs/openspp &&  \
    openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365 -subj "/C=FR/O=krkr/OU=Domain Control Validated/CN=*.krkr.io"
RUN ls /etc/ssl/certs/openspp
WORKDIR /app
COPY . /app
CMD ["python", "main.py"]
