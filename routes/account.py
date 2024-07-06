from flask import Blueprint, render_template, session
from models import db, Giveaway, Participation
from flask_login import login_required, current_user
from datetime import datetime

account_bp = Blueprint('account', __name__)


@account_bp.route('/account')
@login_required
def account():
    """
    Renders the 'account.html' template upon accessing the '/account' route.
    No parameters are passed to this function.
    Returns the rendered 'account.html' template.
    """
    user = current_user
    total_giveaways = Giveaway.query.filter_by(creator_id=user.id).count()
    active_giveaways = Giveaway.query.filter(Giveaway.creator_id == user.id, Giveaway.end_date >= datetime.utcnow()).count()
    participants = Participation.query.join(Giveaway).filter(Giveaway.creator_id == user.id).count()
    prizes_awarded = Giveaway.query.filter_by(creator_id=user.id).filter(Giveaway.end_date < datetime.utcnow()).count()

    return render_template('account.html', user=user, total_giveaways=total_giveaways, active_giveaways=active_giveaways, participants=participants, prizes_awarded=prizes_awarded)