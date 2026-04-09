# Python ka official image use karo
FROM python:3.9-slim

# Container ke andar working directory set karo
WORKDIR /app

# Requirements file copy karo
COPY requirements.txt .

# Dependencies install karo
RUN pip install --no-cache-dir -r requirements.txt

# Saari files copy karo
COPY . .

# Container ka port expose karo
EXPOSE 5000

# App run karo
CMD ["python", "app.py"]