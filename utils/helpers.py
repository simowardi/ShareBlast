from flask import session
from models.user import User
from models.publisher import Publisher

def get_current_user():
    if 'user_id' in session:
        return User.query.get(session['user_id'])
    elif 'publisher_id' in session:
        return Publisher.query.get(session['publisher_id'])
    return None