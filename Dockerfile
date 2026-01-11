FROM python:3.11-slim

WORKDIR /app

# Install system dependencies if needed by scipy/pandas
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY server/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY server/ .

EXPOSE 80

CMD ["python", "server.py"]