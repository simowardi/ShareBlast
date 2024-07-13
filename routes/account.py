from flask import Blueprint, render_template, redirect, url_for, flash
from models import db, Giveaway, Participation
from flask_login import login_required, current_user, logout_user
from datetime import datetime

account_bp = Blueprint('account', __name__)

@account_bp.route('/account')
@login_required
def account():
    """
    Renders the 'account.html' template upon accessing the '/account' route.
    """
    user = current_user
    total_giveaways = Giveaway.query.filter_by(creator_id=user.id).count()
    active_giveaways = Giveaway.query.filter(Giveaway.creator_id == user.id, Giveaway.end_date >= datetime.utcnow).count()
    participants = Participation.query.join(Giveaway).filter(Giveaway.creator_id == user.id).count()
    prizes_awarded = Giveaway.query.filter_by(creator_id=user.id).filter(Giveaway.end_date < datetime.utcnow).count()

    return render_template('account.html', user=user, total_giveaways=total_giveaways, 
                           active_giveaways=active_giveaways, participants=participants, 
                           prizes_awarded=prizes_awarded)


@account_bp.route('/delete_account', methods=['POST'])
@login_required
def delete_account():
    """
    Deletes the user account, commits the deletion to the database, logs out the user, displays a success message, and redirects to the index page.
    """
    user = current_user
    db.session.delete(user)
    db.session.commit()
    logout_user()
    flash('Your account has been successfully deleted.', 'success')
    return redirect(url_for('index'))


@account_bp.route('/user_giveaways')
@login_required
def usergiveaways():
    """
    Renders the 'usergiveaways.html' template to display the user's giveaways.
    """
    user_giveaways = Giveaway.query.filter_by(creator_id=current_user.id).all()
    print(f"Number of giveaways found: {len(user_giveaways)}")  # Debug print
    for giveaway in user_giveaways:
        print(f"Giveaway ID: {giveaway.id}, Title: {giveaway.title}")  # More detailed debug
    return render_template('usergiveaways.html', user_giveaways=user_giveaways)