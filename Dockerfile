# syntax=docker/dockerfile:1
FROM python:3.9
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set workdir
WORKDIR /code

# Copy project files
COPY . /code/

# Install dependencies
RUN pip install -r requirements.txt
