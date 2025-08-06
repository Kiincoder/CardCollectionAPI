from flask import Blueprint, jsonify, request
import jwt
from datetime import datetime, timedelta
from Models.models import usuarios
from Connection.config import Config

criarsessao_bp = Blueprint('criarsessao', __name__)

@criarsessao_bp.route('/criar', methods=["POST"])
def criarsessao():
  """
    Criar uma sessão de usuário
    ---
    tags:
      - Sessão
    consumes:
      - application/json
    parameters:
      - in: body
        name: corpo
        required: true
        schema:
          type: object
          properties:
            email:
              type: string
              example: joao@email.com
            senha:
              type: string
              example: 123456
    responses:
      200:
        description: Retorna o token de sessão do usuário.
        schema:
          type: object
          properties:
            token:
              type: string
              description: Token de sessão do usuário
      401:
        description: Retorna erro se email ou senha não forem fornecidos.
  
  """


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