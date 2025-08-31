from flask import Blueprint, jsonify, request
from models.models import usuarios, colecao, cartas
from models.models import db
from utils.decorator import token_obrigatorio


listarcolecao_bp = Blueprint('listarcolecao', __name__)

@listarcolecao_bp.route('/listar', methods=["GET"])
@token_obrigatorio
def listarcolecao():
  """
  Listar coleção de cartas do usuário.
  ---
  tags:
    - Coleção
  parameters:
    - name: Authorization
      in: header
      type: string
      required: true

  responses:
    200:
      description: Retorna a coleção de cartas do usuário.
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
  """
  
  usuario_id = request.usuario_id
  cartas_usuario = (
        db.session.query(cartas.nome, cartas.raridade, cartas.uri_carta)
        .join(colecao, colecao.cid == cartas.cid)
        .filter(colecao.uid == usuario_id)
        .all()
    )

  cartas_usuario_serializadas = [
        {
            'nome': carta.nome,
            'raridade': carta.raridade,
            'uri_carta': carta.uri_carta
        } for carta in cartas_usuario
    ]

  return jsonify(cartas_usuario_serializadas), 200



