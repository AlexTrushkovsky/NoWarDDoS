# Base image
FROM python:latest

COPY *.py /nowarddos/
COPY requirements.txt /nowarddos/

WORKDIR /nowarddos
RUN pip install -r requirements.txt

ENTRYPOINT ["python", "/nowarddos/updater.py"]
