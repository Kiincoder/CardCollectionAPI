from flask import Blueprint, jsonify, request
import jwt
from datetime import datetime, timedelta
from app import app
from models.models import usuarios

criarsessao_bp = Blueprint('criarsessao', __name__)

@criarsessao_bp.route('api/', methods=["POST"])
def criarsessao():
  response = request.json
  email = response.get('email')
  senha = response.get('senha')

  if not email or not senha:
    return jsonify({'erro': 'Email e senha são obrigatórios'}), 400
  
  usuario = usuarios.query.filter_by(email=email).first()

  if usuario and usuarios.verificar_senha(senha_plana=senha):
    payload = {
        'user_id': usuario.id,
        'exp': datetime.utcnow() + timedelta(hours=2) 
    }
    token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
    return jsonify({'token': token})
  else:
    return jsonify({'erro': 'Credenciais inválidas'}), 401