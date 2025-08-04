
USER = ''
PASSWORD = ''
HOST = ''
DB_NAME = ''

class Config:
    SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{USER}:{PASSWORD}@{HOST}/{DB_NAME}'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = ""