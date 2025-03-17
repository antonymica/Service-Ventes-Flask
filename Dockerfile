# Utilisation d'une image Python optimisée
FROM python:3.11-slim AS builder

# Définition du répertoire de travail
WORKDIR /app

# Installation des dépendances système nécessaires
RUN apt update && apt install -y --no-install-recommends netcat-openbsd && rm -rf /var/lib/apt/lists/*

# Copie et installation des dépendances Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copie des fichiers nécessaires
COPY .env.example /app/.env

# Copie du code source de l'application
COPY . .

# Création d'un utilisateur non-root sécurisé
RUN useradd --no-create-home --shell /usr/sbin/nologin flaskuser && \
    chown -R flaskuser:flaskuser /app

# Ajout du script d'entrée et permissions
COPY entrypoint.sh ./entrypoint.sh
RUN chmod +x ./entrypoint.sh

# Passage à l'utilisateur sécurisé
USER flaskuser

# Exposition du port de l'application
EXPOSE 5000

# Définition du point d'entrée et de la commande de démarrage
ENTRYPOINT ["./entrypoint.sh"]
