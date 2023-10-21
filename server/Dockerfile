# Use the official Python 3.11-slim image as a base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /server

# Copy the dependencies file to the container
COPY ./requirements.txt ./

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the content of the local backend directory to the working directory
COPY ./src ./src

# Set the FLASK_APP environment variable
ENV FLASK_APP=src/main.py