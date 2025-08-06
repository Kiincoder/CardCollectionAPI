from flask import Flask
from Connection.config import Config
from Models.models import db
from Routes.Sessao.criarSessaoBP import criarsessao_bp 
from Routes.Usuario.criarUsuarioBP import criarusuario_bp 
from Routes.Pacote.comprarPacoteBP import comprarpacote_bp
from Routes.Colecao.listarColecaoBP import listarcolecao_bp
from Routes.Colecao.buscarColecaoBP import buscar_colecao_bp
from Routes.Usuario.informacaoUsuarioBP import informacaousuario_bp
from flasgger import Swagger

app = Flask(__name__)
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