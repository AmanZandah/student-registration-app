# Use a small official Python image as the base
FROM python:3.13-slim

# Set the working directory inside the container
WORKDIR /app

# Copy and install dependencies first (lets Docker cache this layer)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt gunicorn

# Copy the rest of the application code
COPY . .

# The app listens on port 5000
EXPOSE 5000

# Run with gunicorn (a production web server), bound to all interfaces
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
