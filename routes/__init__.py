# models/__init__.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_app(app):
    """
    Initializes the Flask application with the database.
     
    Parameters:
        app (Flask): The Flask application to initialize.

    Returns:
        None
    """
    db.init_app(app)
    with app.app_context():
        db.create_all()
