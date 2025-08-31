
from models.models import db

def create_models(app):
    with app.app_context():
        db.create_all()
        print("tabelas criadas")