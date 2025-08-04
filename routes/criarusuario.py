from flask import Blueprint, jsonify, request
from app import app


criarusuario_bp = Blueprint('criarusuario', __name__)

@criarusuario_bp.route('api/', methods=["POST"])
def criarusuario():
  return jsonify({'message': 'oi'}), 200