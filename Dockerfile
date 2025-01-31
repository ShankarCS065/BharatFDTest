# Use Python 3.11 as the base image (Updated from 3.9)
FROM python:3.11

# Set the working directory in the container
WORKDIR /app

# Copy project files
COPY . /app

# Upgrade pip first
RUN python -m pip install --upgrade pip

# Install dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Expose port 8000 (Django default port)
EXPOSE 8000

# Run Django application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
