# Python environment
FROM python:3.11-slim

# Working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y libgomp1 \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install CPU-only PyTorch
RUN pip install --no-cache-dir torch \
    --index-url https://download.pytorch.org/whl/cpu

# Install remaining dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Streamlit port
EXPOSE 8501

# Start application
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]