# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY src /app

# Make port 11500 available to the world outside this container
EXPOSE 11500

# Define environment variable
ENV FLASK_APP=account_service_flask.py

# Run the application
CMD ["waitress-serve", "--host", "0.0.0.0", "--port", "11500", "account_service_flask:app"]