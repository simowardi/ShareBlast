from . import db
from datetime import datetime
from .winner import Winner


class Giveaway(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(256))
    end_date = db.Column(db.DateTime, index=True)
    created_at = db.Column(db.DateTime, default=datetime.now())
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator = db.relationship('User', backref=db.backref('giveaways', lazy=True))
    prize_url = db.Column(db.String(256), nullable=False)


    def __repr__(self):
        return '<Giveaway %r>' % self.title


	# Selects a winner for the giveaway if the giveaway 
    def select_winner(self):
        if not self.winner and datetime.now() >= self.end_date:
            winner = Winner.select_winner(self)
            return winner
        return None
    

    def select_winner(self):
        if not self.winner and datetime.now() >= self.end_date:
            winner = Winner.select_winner(self)
            if winner:
                winner.prize_url = self.prize_url  # Store the prize URL for the winner
                db.session.commit()
            return winner
        return None
