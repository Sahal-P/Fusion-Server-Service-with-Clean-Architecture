FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory to /app
WORKDIR /app

# Copy the requirements file into the container at /app
COPY requirements.txt /app/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt
RUN pip install twisted[http2,tls]

# Copy the rest of the application code into the container at /app
COPY . /app/

# RUN python manage.py kafka_consumer


CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
# CMD [ "python", "manage.py", "kafka_consumer" ]