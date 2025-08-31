USER = 'root'
PASSWORD = ''
HOST = 'localhost'
DB_NAME = 'dev_api'

class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "jorge"