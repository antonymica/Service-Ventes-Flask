from app import create_app

# Création de l'instance de l'application Flask
app = create_app()

if __name__ == "__main__":
    """
    Point d'entrée principal de l'application.
    Lance le serveur Flask en mode debug.
    """
    app.run(debug=False, host='0.0.0.0', port=5000)