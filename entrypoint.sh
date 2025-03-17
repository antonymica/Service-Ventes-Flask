#!/bin/bash

# Arrêt en cas d'erreur
set -e

# Fonction d'attente de la base de données
function wait_for_db() {
  echo "Attente de la base de données..."
  until nc -z db 5432; do
    sleep 1
  done
  echo "Base de données prête !"
}

# Exécuter l'attente et démarrer l'application
wait_for_db

flask db init
flask db migrate -m "Initial migration"
flask db upgrade  # Appliquer les migrations

python run.py
