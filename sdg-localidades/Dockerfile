FROM python:3.12-slim

WORKDIR /app

# Install system deps for pandas/openpyxl
RUN apt-get update && apt-get install -y --no-install-recommends \
    gcc \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY engine/ engine/
COPY webapp/ webapp/
COPY input/ input/
COPY output/ output/

# Expose port
EXPOSE 5000

# Run with waitress production server
CMD ["python", "-m", "waitress", "--host=0.0.0.0", "--port=5000", "webapp.app:app"]
