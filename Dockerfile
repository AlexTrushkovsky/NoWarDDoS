# Base image
FROM python:latest

COPY . /nowarddos/

WORKDIR /nowarddos
RUN pip install -r requirements.txt

ENTRYPOINT ["/bin/sh", "start.sh"]
