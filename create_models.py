from app import app
from Models.models import db

with app.app_context():
    db.create_all()
    print("tabelas criadas")