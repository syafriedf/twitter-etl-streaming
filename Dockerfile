FROM apache/airflow:2.5.0

# Salin requirements.txt ke dalam kontainer
COPY requirements.txt .

# Install dependensi Python
RUN pip install --no-cache-dir -r requirements.txt

# Salin DAGs, logs, dan plugins jika diperlukan
# (Opsional, karena sudah di-mount melalui volumes di docker-compose.yml)
