from flask import Blueprint, jsonify, request
from models.models import usuarios
from models.models import db

criarusuario_bp = Blueprint('criarusuario', __name__)

@criarusuario_bp.route('/', methods=["POST"])
def criarusuario():
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