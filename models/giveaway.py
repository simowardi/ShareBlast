from app import db
from datetime import datetime

class Giveaway(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), index=True)
    description = db.Column(db.Text)
    image_url = db.Column(db.String(256))
    end_date = db.Column(db.DateTime, index=True)
    publisher_id = db.Column(db.Integer, db.ForeignKey('publisher.id'))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)