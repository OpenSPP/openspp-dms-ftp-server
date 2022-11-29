FROM python:3.10-slim-bullseye

ARG OPENSPP_URL
ARG OPENSPP_DB_NAME

ENV OPENSPP_URL $OPENSPP_URL
ENV OPENSPP_DB_NAME $OPENSPP_DB_NAME

COPY requirements.txt /requirements.txt
RUN pip install -r /requirements.txt

COPY . /app

WORKDIR /app
EXPOSE 2121

CMD ["python", "main.py"]
