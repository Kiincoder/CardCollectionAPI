from flask import Blueprint, jsonify, request
from models.models import usuarios, colecao, cartas
from models.models import db
from utils.decorator import token_obrigatorio


listarcolecao_bp = Blueprint('listarcolecao', __name__)

@listarcolecao_bp.route('/', methods=["GET"])
@token_obrigatorio
def listarcolecao():
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



