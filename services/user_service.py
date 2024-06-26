from models.user import User
from models.publisher import Publisher
from app import db

def create_user(username, email, password):
    user = User(username=username, email=email)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    return user

def create_publisher(company_name, email, password):
    publisher = Publisher(company_name=company_name, email=email)
    publisher.set_password(password)
    db.session.add(publisher)
    db.session.commit()
    return publisher

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_publisher_by_company_name(company_name):
    return Publisher.query.filter_by(company_name=company_name).first()