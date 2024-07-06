from datetime import datetime
from app import db
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    giveaway_id = db.Column(db.Integer, db.ForeignKey('giveaway.id'), nullable=False)
    participated_at = db.Column(db.DateTime, default=datetime.utcnow)
