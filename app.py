from flask import Flask
from connection.config import Config
from models.models import db
from routes.criarsessao import criarsessao_bp
from routes.criarusuario import criarusuario_bp

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

app.register_blueprint(criarsessao_bp, url_prefix='/criarsessao')
app.register_blueprint(criarusuario_bp, url_prefix='/criarusuario')

if __name__ == '__main__':
    app.run(debug=True)