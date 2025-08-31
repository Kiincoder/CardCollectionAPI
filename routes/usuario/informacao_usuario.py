from flask import Blueprint, jsonify, request
from models.models import usuarios
from models.models import db
from utils.decorator import token_obrigatorio

informacaousuario_bp = Blueprint('informacaousuario', __name__)

@informacaousuario_bp.route('/informacao', methods=["GET"])
@token_obrigatorio
def informacao_usuario():
    """
    Obter informações do usuário autenticado.
    ---
    tags:
      - Usuário
    parameters:
      - name: Authorization
        in: header
        type: string
        required: true
    responses:
      200:
        description: Retorna as informações do usuário.
        schema:
          type: object
          properties:
            nome:
              type: string
              description: Nome do usuário
            uri_foto:
              type: string
              description: URI da foto do usuário
    
    """


    usuario_id = request.usuario_id
    usuario = db.session.query(usuarios).filter_by(uid=usuario_id).first()
    
    if not usuario:
        return jsonify({'erro': 'Usuário não encontrado!'}), 404
    
    usuario_info = {
      'nome': usuario.nome,
      'uri_foto': usuario.uri_foto
    }
    
    return jsonify(usuario_info), 200