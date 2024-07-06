from datetime import datetime
from . import db


class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    giveaway_id = db.Column(db.Integer, db.ForeignKey('giveaway.id'), nullable=False)
    participated_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('participations', lazy=True))
    giveaway = db.relationship('Giveaway', backref=db.backref('participations', lazy=True))

    def __repr__(self):
        return f'<Participation user_id={self.user_id} giveaway_id={self.giveaway_id}>'

