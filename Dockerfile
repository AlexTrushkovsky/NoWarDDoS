# Base image
FROM python:3.8.2-alpine

COPY *.py /nowarddos/
COPY *.env /nowarddos/
COPY requirements.txt /nowarddos/

WORKDIR /nowarddos
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/nowarddos/attack.py"]
