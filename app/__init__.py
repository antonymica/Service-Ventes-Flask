from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from app.config import Config
from app.database import db
from app.routes import register_routes

def create_app():
    """
    Initialise et configure l'application Flask.
    - Charge la configuration depuis l'objet Config.
    - Initialise la base de données avec SQLAlchemy.
    - Active la gestion des migrations avec Flask-Migrate.
    - Active le support CORS pour les requêtes cross-origin.
    - Enregistre les routes de l'application.
    
    Retourne :
        app (Flask) : L'application Flask configurée.
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialisation de la base de données
    db.init_app(app)
    Migrate(app, db)
    
    # Activation de CORS pour permettre les requêtes externes
    CORS(app)
    
    # Enregistrement des routes
    register_routes(app)
    
    return app
