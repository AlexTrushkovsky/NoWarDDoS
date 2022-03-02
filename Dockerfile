# Base image
FROM python:alpine

COPY *.py /nowarddos/
COPY requirements.txt /nowarddos/

WORKDIR /nowarddos
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/nowarddos/attack.py"]
