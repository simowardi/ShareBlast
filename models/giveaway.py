from . import db
from datetime import datetime
from .winner import Winner
from .participation import Participation

 

class Giveaway(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(256))
    end_date = db.Column(db.DateTime, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator = db.relationship('User', backref=db.backref('giveaways', lazy=True))

    # Relationships
    winner = db.relationship('Winner', backref=db.backref('giveaway', uselist=False))
    participations = db.relationship('Participation', backref=db.backref('giveaway', lazy=True))

    def __repr__(self):
        return '<Giveaway %r>' % self.title
