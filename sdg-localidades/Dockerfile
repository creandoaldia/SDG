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

# Auth configuration (must be set via env or docker-compose)
ENV FLASK_SECRET_KEY=""
ENV APP_PASSWORD=""
ENV APPLICATION_ROOT="/sdg/"
ENV SESSION_COOKIE_PATH="/sdg/"
ENV HTTPS="false"
ENV SESSION_LIFETIME_HOURS="8"

# Expose port
EXPOSE 5000

# Run with waitress production server (single worker para tab_states thread safety)
CMD ["python", "-m", "waitress", "--host=0.0.0.0", "--port=5000", "--workers=1", "webapp.app:app"]
