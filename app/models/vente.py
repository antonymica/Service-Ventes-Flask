# Importation du module de gestion de la base de données
from app.database import db

class Vente(db.Model):
    """
    Modèle représentant une vente dans la base de données.
    Chaque vente est associée à un produit avec une quantité et un prix.
    """
    __tablename__ = 'ventes'  # Nom de la table dans la base de données
    
    id = db.Column(db.Integer, primary_key=True)  # Clé primaire unique pour chaque vente
    numero_produit = db.Column(db.String(50), nullable=False)  # Numéro de référence du produit
    designation = db.Column(db.String(100), nullable=False)  # Nom ou description du produit
    prix_unitaire = db.Column(db.Float, nullable=False)  # Prix unitaire du produit
    quantite_vendue = db.Column(db.Integer, nullable=False)  # Quantité vendue
    
    def to_dict(self):
        """
        Convertit l'objet Vente en dictionnaire pour une manipulation plus facile.
        Retourne les informations de la vente sous forme de dictionnaire.
        """
        return {
            "id": self.id,
            "numero_produit": self.numero_produit,
            "designation": self.designation,
            "prix_unitaire": self.prix_unitaire,
            "quantite_vendue": self.quantite_vendue,
            "montant_total": self.prix_unitaire * self.quantite_vendue  # Calcul automatique du montant total
        }
        