from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)

from routes import main, auth, giveaway

app.register_blueprint(main.bp)
app.register_blueprint(auth.bp)
app.register_blueprint(giveaway.bp)

if __name__ == '__main__':
    app.run(debug=True)