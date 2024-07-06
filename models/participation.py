from datetime import datetime
from . import db
from flask_login import UserMixin


class Participation(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    giveaway_id = db.Column(db.Integer, db.ForeignKey('giveaway.id'), nullable=False)
    participated_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('participations', lazy=True))
    giveaway = db.relationship('Giveaway', backref=db.backref('participations', lazy=True))

    def __repr__(self):
        return f'<User id={self.id}>'
