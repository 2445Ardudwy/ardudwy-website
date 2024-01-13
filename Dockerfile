# Use an official Python runtime as a parent image
FROM python:3.10-alpine3.16

# Install the packages necessary for mysqlclient
RUN apk add --no-cache mariadb-dev build-base

# Copy the requirements file into the container at /tmp/
COPY ./requirements.txt /tmp/

# Install any needed packages specified in requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r /tmp/requirements.txt

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY ./project /app

# Expose port 8000 for Daphne
EXPOSE 8000

# Run Daphne ASGI server
CMD ["daphne", "-b", "0.0.0.0", "-p", "8000", "core.asgi:application"]

