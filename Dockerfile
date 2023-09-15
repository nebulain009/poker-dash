# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=myproject.settings
ENV DJANGO_SECRET_KEY=your_secret_key
ENV DJANGO_DEBUG=False

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Expose port 8000 for the Django development server
EXPOSE 8000

# Start the Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
