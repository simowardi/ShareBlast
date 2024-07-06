# routes/__init__.py
from flask import Blueprint

# Initialize the blueprints
auth_bp = Blueprint('auth', __name__)
giveaway_bp = Blueprint('giveaway', __name__)
account_bp = Blueprint('account', __name__)

# Import routes to register them with blueprints
from . import auth
from . import giveaway
from . import account
