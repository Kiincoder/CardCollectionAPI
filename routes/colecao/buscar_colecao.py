from flask import Blueprint, jsonify, request
from models.models import cartas, colecao, usuarios, db
from utils.decorator import token_obrigatorio


buscar_colecao_bp = Blueprint('buscar_colecao', __name__)

@buscar_colecao_bp.route('/buscar/<string:nome>', methods=['GET'])
@token_obrigatorio
def buscar_colecao(nome):
  """ 
  Buscar coleção de cartas de um usuário específico
  ---
  tags:
    - Coleção
  parameters:
    - name: nome
      in: path
      type: string
      required: true
      description: Nome do usuário desejado
  responses:
    200:
      description: Retorna a coleção de cartas do usuário desejado
      schema:
        type: array
        items:
          type: object
          properties:
            nome:
              type: string
              description: Nome da carta
            raridade:
              type: string
              description: Raridade da carta
            uri_carta:
              type: string
              description: URI da carta
    404:
      description: Usuário não encontrado ou coleção vazia
  
  """


  usuario_procurado = db.session.query(usuarios.uid).filter(usuarios.nome == nome).first()
  if not usuario_procurado:
    return jsonify({'erro': 'Usuário não encontrado!'}), 404
  
  colecao_usuario = db.session.query(cartas.nome, cartas.raridade, cartas.uri_carta).join(colecao, colecao.cid == cartas.cid).filter(colecao.uid == usuario_procurado.uid).all()

  if not colecao_usuario:
    return jsonify({'erro': 'Não foi encontrada nenhuma coleção para o usuário!'}), 404
  
  colecao_usuario_serializada = [
        {
            'nome': carta.nome,
            'raridade': carta.raridade,
            'uri_carta': carta.uri_carta
        } for carta in colecao_usuario
    ]
  
  return jsonify(colecao_usuario_serializada), 200