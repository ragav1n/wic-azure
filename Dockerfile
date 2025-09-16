# Use lightweight official Python image
FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

# Force Flask to bind to 0.0.0.0
CMD ["python", "app.py", "--host=0.0.0.0", "--port=5000"]
