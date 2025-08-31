from flask import Blueprint, jsonify, request
from models.models import usuarios
from models.models import db

criarusuario_bp = Blueprint('criarusuario', __name__)

@criarusuario_bp.route('/criar', methods=["POST"])
def criarusuario():
  """
    Criar um novo usuário
    ---
    tags:
      - Usuário
    consumes:
      - application/json
    parameters:
      - in: body
        name: corpo
        required: true
        schema:
          type: object
          properties:
            nome:
              type: string
              example: João
            email:
              type: string
              example: joao@email.com
            senha:
              type: string
              example: 123456
    responses:
      200:
        description: Retorna uma mensagem de sucesso ao criar o usuário.
        schema:
          type: object
          properties:
            mensagem:
              type: string
              description: Mensagem de sucesso
      400:
        description: Retorna erro se os dados estiverem incompletos ou se o email já estiver cadastrado.
        schema:
          type: object
          properties:
            mensagem:
              type: string
              description: Mensagem de erro




  """

  data = request.get_json()
  if not data or not all(k in data for k in ('email', 'senha', 'nome')):
    return jsonify({'mensagem': 'Dados incompletos!'}), 400
  
  if usuarios.query.filter_by(email=data['email']).first():
    return jsonify({'mensagem': 'Email já cadastrado!'}), 400
  
  usuario = usuarios(
    email= data['email'],
    senha= usuarios.encrypt_senha(data['senha']),
    nome = data['nome']  
  )
  db.session.add(usuario)
  db.session.commit()
  return jsonify({'mensagem': 'Usuário criado com sucesso!'}), 200