from flask import Blueprint, request, render_template, redirect, url_for, session
from models import db
from models.giveaway import Giveaway
from models.participation import Participation
from datetime import datetime

giveaway_bp = Blueprint('giveaway', __name__)

@giveaway_bp.route('/create-giveaway', methods=['GET', 'POST'])
def create_giveaway():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image_url = request.form['picture']
        end_date = datetime.strptime(request.form['endTime'], '%Y-%m-%dT%H:%M')
        user_id = session.get('user_id')
        
        new_giveaway = Giveaway(
            title=title,
            description=description,
            image_url=image_url,
            end_date=end_date,
            creator_id=user_id
        )
        db.session.add(new_giveaway)
        db.session.commit()

        return render_template('giveaway_created.html', giveaway_id=new_giveaway.id)

    return render_template('create_giveaway.html')

@giveaway_bp.route('/giveaway/<int:giveaway_id>', methods=['GET'])
def view_giveaway(giveaway_id):
    giveaway = Giveaway.query.get_or_404(giveaway_id)
    return render_template('giveaway.html', giveaway=giveaway)

@giveaway_bp.route('/enter-giveaway/<int:giveaway_id>', methods=['POST'])
def enter_giveaway(giveaway_id):
    """
    Check if the user is logged in
    Get the user ID from the session
    Check if the user has already entered the giveaway
    Record the user's entry
    """
    # Check if the user is logged in
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    # Get the user ID from the session
    user_id = session['user_id']
    giveaway = Giveaway.query.get_or_404(giveaway_id)

    # Check if the user has already entered the giveaway
    participation = Participation.query.filter_by(user_id=user_id, giveaway_id=giveaway_id).first()
    if participation:
        return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway.id))

    # Record the user's entry
    new_participation = Participation(user_id=user_id, giveaway_id=giveaway_id)
    db.session.add(new_participation)
    db.session.commit()

    return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway.id))
