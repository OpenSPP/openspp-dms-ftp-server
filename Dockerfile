FROM python:3.10-slim-bullseye as base

FROM base as builder
RUN apt update -y && apt install --no-install-recommends openssl

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN mkdir -p /etc/ssl/certs/openspp &&  \
    cd /etc/ssl/certs/openspp &&  \
    openssl req -x509 -newkey rsa:4096 -nodes -out server.crt -keyout server.key -days 365 -subj "/C=FR/O=krkr/OU=Domain Control Validated/CN=*.krkr.io"
RUN ls /etc/ssl/certs/openspp
WORKDIR /app
COPY . /app

FROM builder as production
CMD ["python", "main.py"]

FROM builder as development
CMD ["python", "main.py"]

FROM builder as test
COPY requirements-test.txt /requirements-test.txt
RUN pip install -r /requirements-test.txt
CMD ["pytest", "-v", "-s", "--cov=openspp_dms_ftp_server", "--cov-report=term-missing", "--cov-fail-under=97", "--cov-branch", "--cov-report=xml", "--cov-report=html", "--cov-report=annotate", "--junitxml=tests.xml", "openspp_dms_ftp_server/tests/"]
