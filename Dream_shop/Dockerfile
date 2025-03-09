FROM python:3.9-slim

WORKDIR /app

# Installation des dépendances système pour mysqlclient
RUN apt-get update && apt-get install -y default-libmysqlclient-dev build-essential pkg-config

# Copie des fichiers de dépendances et installation
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie du code source
COPY . .

# Variables d'environnement
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=dream_shop.settings

# Exposition du port
EXPOSE 8000

# Commande de démarrage
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"] 