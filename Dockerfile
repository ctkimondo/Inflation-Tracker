# Official python "Base Image"
FROM python:3.11-slim

# Set "Work Directory" inside the container
WORKDIR /app

# Copy manifest and install libraries
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy your source code and data folder
COPY src/ ./src/
COPY data/ ./data/

# Command that runs when the container starts
CMD ["python", "src/main.py"]