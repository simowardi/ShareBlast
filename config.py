import os


class Config:
    SECRET_KEY = os.environ.get('az12', '123456789AZERTYUIOP')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:zeé"ZE2323@localhost/my_flask_app'
    SQLALCHEMY_TRACK_MODIFICATIONS = False