# Use a lightweight Python base image
FROM python:3.10-slim

# Set working directory inside the container
WORKDIR /app

# Copy project files to the container
COPY . /app

# Install dependencies (update if you have requirements.txt)
RUN pip install --no-cache-dir flask
RUN pip install -r requirements.txt
# Expose the Flask port
EXPOSE 8081

# Run the Flask app
CMD ["python", "run.py"]
