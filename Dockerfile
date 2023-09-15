# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables for Django
ENV DJANGO_SETTINGS_MODULE=pokerdash.settings
ENV DJANGO_SECRET_KEY='django-insecure-g@g7!brjf_4z2q&nf)po$l#((m%p_b29@)+_^l=qy%20z*+%l+'
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
