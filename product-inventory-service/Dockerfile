# Use official Python image
FROM python:3.11
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

# First populate the database, then start the consumer service
CMD ["sh", "-c", "python -m src.db.db && python -m src.main"]

