FROM python:3.10-slim-buster

# Set up environment
WORKDIR /app

# Install system dependencies
RUN apt-get update -y && \
    apt-get install -y awscli && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy remaining files
COPY . .

# Expose port (assuming your app uses 8080 based on your run command)
EXPOSE 8080

# Run the application
CMD ["python3", "app.py"]