from datetime import datetime
import random
from . import db
from flask_login import UserMixin

class Winner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    giveaway_id = db.Column(db.Integer, db.ForeignKey('giveaway.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    selected_at = db.Column(db.DateTime, default=datetime.utcnow())

    giveaway = db.relationship('Giveaway', backref=db.backref('winner', uselist=False))
    user = db.relationship('User')

    def __repr__(self):
        return '<Winner %r>' % self.id

    @staticmethod
    def select_winner(giveaway):
        """
        Selects a winner for a giveaway if the giveaway 
        has not already been won and the current time is after the end date.
        Parameters:
            giveaway (Giveaway): The giveaway for which to select a winner.
        Returns:
            Winner or None: The winner of the giveaway if one was selected, otherwise None.
        """
        if not giveaway.winner and datetime.utcnow >= giveaway.end_date:
            participants = [p.user for p in giveaway.participations]
            if participants:
                winner_user = random.choice(participants)
                winner = Winner(giveaway_id=giveaway.id, user_id=winner_user.id)
                db.session.add(winner)
                db.session.commit()
                return winner
        return None
