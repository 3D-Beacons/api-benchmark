FROM python:3.9.1-slim-buster

# Install dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /app

COPY locustfile.py .
COPY utils.py .

CMD ["locust", "--config", "conf/locust.conf"]
