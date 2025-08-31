from flask import Flask
from connection.config import Config
from models.models import db
from routes.sessao.criar_sessao import criarsessao_bp 
from routes.usuario.criar_usuario import criarusuario_bp 
from routes.pacote.comprar_pacote import comprarpacote_bp
from routes.colecao.listar_colecao import listarcolecao_bp
from routes.colecao.buscar_colecao import buscar_colecao_bp
from routes.usuario.informacao_usuario import informacaousuario_bp
from flasgger import Swagger
from create_models import create_models

app = Flask(__name__)
create_models(app=app)
swagger = Swagger(app)
app.config.from_object(Config)
db.init_app(app)

#Rotas de sessao
app.register_blueprint(criarsessao_bp, url_prefix='/sessao')

#Rotas de usuario
app.register_blueprint(criarusuario_bp, url_prefix='/usuario')
app.register_blueprint(informacaousuario_bp, url_prefix='/usuario')

#Rotas pacotinhos
app.register_blueprint(comprarpacote_bp, url_prefix='/pacote')

#Rotas de colecao
app.register_blueprint(listarcolecao_bp, url_prefix='/colecao')
app.register_blueprint(buscar_colecao_bp, url_prefix='/colecao')

if __name__ == '__main__':
    app.run(debug=True)