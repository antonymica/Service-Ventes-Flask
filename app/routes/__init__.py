from app.routes.routes import vente_bp

def register_routes(app):
    app.register_blueprint(vente_bp, url_prefix='/ventes')
