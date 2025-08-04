from flask_sqlalchemy import SQLAlchemy
import bcrypt

db = SQLAlchemy()

class usuarios(db.Model):
  __tablename__ = 'usuarios'

  uid = db.Column(db.Integer, primary_key=True)
  email = db.Column(db.String(120), unique=True, nullable=False)
  senha = db.Column(db.String(120), nullable=False)
  nome = db.Column(db.String(50), nullable=False)
  uri_foto = db.Column(db.String(250), nullable=True)

  def set_senha(self, senha_plana):
    self.senha = bcrypt.hashpw(senha_plana.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

  def verificar_senha(self, senha_plana):
    return bcrypt.checkpw(senha_plana.encode('utf-8'), self.senha.encode('utf-8'))

class cartas(db.Model):
  __tablename__ = 'cartas'

  cid = db.Column(db.Integer, primary_key=True)
  nome = db.Column(db.String(120), unique=True, nullable=False)
  uri_carta = db.Column(db.String(120), unique=True, nullable=False)
  raridade = db.Column(db.Enum(
    "Comum", "Incomum", "Rara", "Ultra rara", "Secreta rara",
    name="raridade_enum"),
  nullable=False)

class colecao(db.Model):
  __tablename__ = 'colecao'

  colid = db.Column(db.Integer, primary_key=True)
  uid = db.Column(db.Integer, db.ForeignKey('usuarios.uid'), nullable=False) 
  cid = db.Column(db.Integer, db.ForeignKey('cartas.cid'), nullable=False) 

