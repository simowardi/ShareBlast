from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import db
from models.giveaway import Giveaway
from models.participation import Participation
from datetime import datetime
from flask_login import login_required, current_user

giveaway_bp = Blueprint('giveaway', __name__)

@giveaway_bp.route('/create-giveaway', methods=['GET', 'POST'])
@login_required
def create_giveaway():
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image_url = request.form['picture']
        end_date = datetime.strptime(request.form['endTime'], '%Y-%m-%dT%H:%M')
        
        new_giveaway = Giveaway(
            title=title,
            description=description,
            image_url=image_url,
            end_date=end_date,
            creator_id=current_user.id
        )
        db.session.add(new_giveaway)
        db.session.commit()

        flash('Giveaway created successfully!', 'success')
        return redirect(url_for('giveaway.view_giveaway', giveaway_id=new_giveaway.id))

    return render_template('create_giveaway.html')

@giveaway_bp.route('/giveaway/<int:giveaway_id>', methods=['GET'])
def view_giveaway(giveaway_id):
    giveaway = Giveaway.query.get_or_404(giveaway_id)
    return render_template('giveaway.html', giveaway=giveaway)

@giveaway_bp.route('/enter-giveaway/<int:giveaway_id>', methods=['POST'])
@login_required
def enter_giveaway(giveaway_id):
    giveaway = Giveaway.query.get_or_404(giveaway_id)

    # Check if the user has already entered the giveaway
    participation = Participation.query.filter_by(user_id=current_user.id, giveaway_id=giveaway_id).first()
    if participation:
        flash('You have already entered this giveaway.', 'info')
        return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway.id))

    # Record the user's entry
    new_participation = Participation(user_id=current_user.id, giveaway_id=giveaway_id)
    db.session.add(new_participation)
    db.session.commit()

    flash('You have successfully entered the giveaway!', 'success')
    return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway.id))