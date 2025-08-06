from functools import wraps
from flask import request, jsonify
from Connection.config import Config
import jwt

def token_obrigatorio(f):
    @wraps(f)
    def decorator(*args, **kwargs):
        auth_header = request.headers.get('Authorization')

        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'erro': 'Token ausente ou inválido'}), 401

        token = auth_header.split(' ')[1]

        try:
            payload = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            request.usuario_id = payload['user_id'] 
        except jwt.ExpiredSignatureError:
            return jsonify({'erro': 'Token expirado'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'erro': 'Token inválido'}), 401

        if not auth_header or not auth_header.startswith('Bearer '):
            return jsonify({'erro': 'Token ausente ou inválido'}), 401

        token = auth_header.split(' ')[1]

        return f(*args, **kwargs)

    return decorator