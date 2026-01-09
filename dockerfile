# Use official Python image
FROM python:3.13.11

# Set working directory
WORKDIR /app

# Copy all files to container
COPY . . 

# Command to run Python file
CMD ["python", "app.py"]
