from models.giveaway import Giveaway
from app import db

def create_giveaway(title, description, image_url, end_date, publisher_id):
    giveaway = Giveaway(title=title, description=description, image_url=image_url, end_date=end_date, publisher_id=publisher_id)
    db.session.add(giveaway)
    db.session.commit()
    return giveaway

def get_giveaway_by_id(giveaway_id):
    return Giveaway.query.get(giveaway_id)

def get_active_giveaways():
    return Giveaway.query.filter(Giveaway.end_date > datetime.utcnow()).all()