from flask import Blueprint, jsonify, request
import jwt
from datetime import datetime, timedelta
from models.models import usuarios
from connection.config import Config

criarsessao_bp = Blueprint('criarsessao', __name__)

@criarsessao_bp.route('/', methods=["POST"])
def criarsessao():
  data = request.get_json()
  email = data['email']
  senha = data['senha']

  if not email or not senha:
    return jsonify({'erro': 'Email e senha são obrigatórios'}), 400
  
  usuario = usuarios.query.filter_by(email=email).first()

  if usuario and usuarios.verificar_senha(senha, usuario.senha):
    payload = {
        'user_id': usuario.uid,
        'exp': datetime.utcnow() + timedelta(hours=2) 
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    return jsonify({'token': token}), 200
  else:
    return jsonify({'erro': 'Credenciais inválidas'}), 401