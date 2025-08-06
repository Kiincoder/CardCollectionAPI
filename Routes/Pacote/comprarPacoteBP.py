from flask import Blueprint, jsonify, request
from Models.models import cartas, colecao, usuarios, db
from Utils.decorator import token_obrigatorio
import random

comprarpacote_bp = Blueprint('comprarpacote', __name__)

@comprarpacote_bp.route('/comprar', methods=["GET"])
@token_obrigatorio
def comprarpacote():
    """
        Comprar um pacote de cartas.
        ---
        tags:
            - Pacote
        parameters:
            - name: Authorization
              in: header
              type: string
              required: true
        responses:
            200:
                description: Retorna as cartas do pacote comprado.
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


    todas_cartas = {
        'Comum': db.session.query(cartas).filter_by(raridade='Comum').all(),
        'Incomum': db.session.query(cartas).filter_by(raridade='Incomum').all(),
        'Rara': db.session.query(cartas).filter_by(raridade='Rara').all(),
        'Ultra rara': db.session.query(cartas).filter_by(raridade='Ultra rara').all(),
        'Secreta rara': db.session.query(cartas).filter_by(raridade='Secreta rara').all(),
    }
    probabilidades = {
        'Comum': 30 / 115,
        'Incomum': 15 / 115,
        'Rara': 10 / 115,
        'Ultra rara': 2 / 115,
        'Secreta rara': 1 / 115,
    }
    pacote = []
    for _ in range(5):
        raridade_escolhida = random.choices(
            population=list(probabilidades.keys()),
            weights=list(probabilidades.values()),
            k=1
        )[0]

        cartas_raridade = todas_cartas[raridade_escolhida]
        if cartas_raridade: 
            carta_sorteada = random.choice(cartas_raridade)
            pacote.append(carta_sorteada)

    usuario_id = request.usuario_id
    pacote_serializado = []
    for carta in pacote:
      add_colecao = colecao(
          uid = usuario_id,
          cid = carta.cid
      )
      db.session.add(add_colecao)    

      pacote_serializado.append({
          'nome': carta.nome,
          'uri_carta': carta.uri_carta,
          'raridade': carta.raridade,
      })

    db.session.commit()
    
    return jsonify(pacote_serializado), 200

