# Base image
FROM python:3.7-slim AS compile-image

# Update dependencies of the build environment
RUN apt-get update && apt-get install -y --no-install-recommends build-essential gcc

# Copy requirements.txt
COPY requirements.txt ./

# Install python dependencies
RUN pip install --user -r requirements.txt

# Stage 2
FROM python:3.7-slim AS build-image

# Copy the installed python dependencies
COPY --from=compile-image /root/.local /root/.local

# Set working directory
WORKDIR /nowarddos

# Copy the source code
COPY *.py ./

ENTRYPOINT ["python", "/nowarddos/updater.py"]
