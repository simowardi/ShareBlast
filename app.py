from flask import Flask
from models import init_app
from routes import auth_bp, giveaway_bp, account_bp


app = Flask(__name__)


# Configure SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:zeé"ZE2323@localhost/my_flask_app'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Initialize app with SQLAlchemy
init_app(app)


# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(giveaway_bp)
app.register_blueprint(account_bp)


# Initialize database tables
with app.app_context():
    db.create_all()


if __name__ == '__main__':
        app.run(debug=True)
