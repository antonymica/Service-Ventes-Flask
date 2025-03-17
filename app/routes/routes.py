# routes.py
from flask import Blueprint, request, jsonify
from app.database import db
from app.models.vente import Vente

# Création du Blueprint pour les routes liées aux ventes
vente_bp = Blueprint("ventes", __name__)

@vente_bp.route("/", methods=["GET"])
def get_ventes():
    """
    Récupère la liste de toutes les ventes enregistrées dans la base de données.
    Retourne un tableau d'objets JSON représentant chaque vente.
    """
    ventes = Vente.query.all()
    return jsonify([vente.to_dict() for vente in ventes])

@vente_bp.route("/", methods=["POST"])
def add_vente():
    """
    Ajoute une nouvelle vente à la base de données.
    Reçoit les informations de la vente en JSON dans la requête.
    """
    data = request.get_json()
    nouvelle_vente = Vente(
        numero_produit=data["numero_produit"],
        designation=data["designation"],
        prix_unitaire=data["prix_unitaire"],
        quantite_vendue=data["quantite_vendue"]
    )
    db.session.add(nouvelle_vente)
    db.session.commit()
    return jsonify(nouvelle_vente.to_dict()), 201

@vente_bp.route("/<int:id_vente>", methods=["GET"])
def get_vente_by_id(id_vente):
    """
    Récupère une vente spécifique en fonction de son ID.
    Retourne une erreur 404 si la vente n'existe pas.
    """
    vente = Vente.query.get_or_404(id_vente)
    return jsonify(vente.to_dict())

@vente_bp.route("/<int:id_vente>", methods=["PUT"])
def update_vente(id_vente):
    """
    Met à jour les informations d'une vente existante.
    Reçoit les nouvelles valeurs en JSON et applique les modifications.
    """
    vente = Vente.query.get_or_404(id_vente)
    data = request.get_json()
    vente.numero_produit = data.get("numero_produit", vente.numero_produit)
    vente.designation = data.get("designation", vente.designation)
    vente.prix_unitaire = data.get("prix_unitaire", vente.prix_unitaire)
    vente.quantite_vendue = data.get("quantite_vendue", vente.quantite_vendue)
    db.session.commit()
    return jsonify(vente.to_dict())

@vente_bp.route("/<int:id_vente>", methods=["DELETE"])
def delete_vente(id_vente):
    """
    Supprime une vente de la base de données en fonction de son ID.
    Retourne un message de confirmation en JSON.
    """
    vente = Vente.query.get_or_404(id_vente)
    db.session.delete(vente)
    db.session.commit()
    return jsonify({"message": "Vente supprimée avec succès"})