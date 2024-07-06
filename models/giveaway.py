from app import db
from datetime import datetime

db = SQLAlchemy()


class Giveaway(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True, nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_url = db.Column(db.String(256))
    end_date = db.Column(db.DateTime, index=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    creator_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    creator = db.relationship('User', backref=db.backref('giveaways', lazy=True))

    def __repr__(self):
        return '<Giveaway %r>' % self.title
