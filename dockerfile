FROM python:3.9-slim

WORKDIR /app

# Copy both the app and the test file
COPY student.py test_student.py ./

# Run the app by default
CMD ["python", "-u", "student.py"]