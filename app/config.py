import os
from dotenv import load_dotenv

# Chargement des variables d'environnement depuis le fichier .env
load_dotenv()

class Config:
    """
    Classe de configuration de l'application.
    Les paramètres sont chargés depuis les variables d'environnement.
    """
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")  # URL de la base de données
    SQLALCHEMY_TRACK_MODIFICATIONS = False  # Désactivation du suivi des modifications pour optimiser les performances
