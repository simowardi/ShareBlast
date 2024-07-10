import os

class Config:
<<<<<<< HEAD
    SECRET_KEY = os.environ.get('az12', '123456789AZERTYUIOP')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'mysql://root:zeé"ZE2323@localhost/my_flask_app')
=======
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///shareblast.db'
>>>>>>> refs/remotes/origin/master
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
# not used for now , but can be used later