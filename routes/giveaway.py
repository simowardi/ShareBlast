from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import db
from models.winner import Winner
from models.giveaway import Giveaway
from models.participation import Participation
from flask_login import login_required, current_user
from datetime import datetime


giveaway_bp = Blueprint('giveaway', __name__)


@giveaway_bp.route('/create-giveaway', methods=['GET', 'POST'])
@login_required
def create_giveaway():
    """
    Creates a new giveaway based on the form data provided by the user.
    If the request method is POST, extracts the title, description, image URL, and end date from the form data.
    Creates a new Giveaway object with the extracted data and the current user as the creator.
    Adds the new giveaway to the database and commits the transaction.
    Flashes a success message for creating the giveaway and redirects to view the created giveaway.
    Returns the create_giveaway.html template if the request method is not POST.
    """
    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image_url = request.form['picture']
        end_date = datetime.strptime(request.form['endTime'], '%Y-%m-%dT%H:%M')
        prize_url = request.form['prize_url']

        new_giveaway = Giveaway(
            title=title,
            description=description,
            image_url=image_url,
            end_date=end_date,
            creator_id=current_user.id
            prize_url=prize_url
        )
        db.session.add(new_giveaway)
        db.session.commit()

        giveaway_url = url_for('giveaway.view_giveaway', giveaway_id=new_giveaway.id, _external=True)
        return render_template('giveaway_created.html', giveaway_url=giveaway_url)

    return render_template('create_giveaway.html')


@giveaway_bp.route('/giveaway/<int:giveaway_id>', methods=['GET'])
def view_giveaway(giveaway_id):
    """
    Route for viewing a specific giveaway.
    Parameters:
        giveaway_id (int): The ID of the giveaway to view.
    Returns:
        The rendered 'giveaway.html' template with the giveaway object.
    Raises:
        NotFound: If the giveaway with the given ID is not found in the database.
    """
    giveaway = Giveaway.query.get_or_404(giveaway_id)
         
    if datetime.now() >= giveaway.end_date:
        winner = giveaway.select_winner()
    else:
        winner = None

    return render_template('giveaway.html', giveaway=giveaway, winner=winner, now=datetime.now())


@giveaway_bp.route('/enter-giveaway/<int:giveaway_id>', methods=['POST'])
@login_required
def enter_giveaway(giveaway_id):
    """
    Route for users to enter a giveaway.
    Parameters:
    - giveaway_id (int): The ID of the giveaway to enter.
    Returns:
    - redirect: A redirect to the giveaway view page.
    Raises:
    - NotFound: If the giveaway with the given ID is not found in the database.
    """
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


@giveaway_bp.route('/select_winner/<int:giveaway_id>', methods=['POST'])
@login_required
def select_winner(giveaway_id):
    """
    Selects a winner for a giveaway if 
    the giveaway has not already been won and the current user is the creator of the giveaway.
    Args:
        giveaway_id (int): The ID of the giveaway for which to select a winner.
    Returns:
        Redirects to the message indicating the winner.
    """
    giveaway = Giveaway.query.get_or_404(giveaway_id)
    if current_user.id != giveaway.creator_id:
        flash('You are not authorized to select the winner for this giveaway.', 'danger')
        return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway_id))

    winner = giveaway.select_winner()
    if winner:
        flash(f'The winner is {winner.user.username}', 'success')
    else:
        flash('No participants found or giveaway not yet ended.', 'warning')

    return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway_id))


@giveaway_bp.route('/my-prizes', methods=['GET'])
@login_required
def my_prizes():
    user_prizes = Winner.query.filter_by(user_id=current_user.id).all()
    return render_template('my_prizes.html', prizes=user_prizes)


@giveaway_bp.route('/giveaway/<int:giveaway_id>/leads', methods=['GET'])
@login_required
def view_leads(giveaway_id):
    """
    Renders the leads page for a specific giveaway by 
    querying the participations and extracting the usernames and emails of participants.
    Parameters:
    - giveaway_id: int - The ID of the giveaway for which to view the leads.
    Returns:
    - Rendered template: giveaway_leads.html - list (usernames and emails).
    """
    giveaway = Giveaway.query.get_or_404(giveaway_id)
    if current_user.id != giveaway.creator_id:
        flash('You are not authorized to view the leads for this giveaway.', 'danger')
        return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway_id))
    
    participations = Participation.query.filter_by(giveaway_id=giveaway_id).all()
    leads = [(p.user.username, p.user.email) for p in participations]

    return render_template('giveaway_leads.html', giveaway=giveaway, leads=leads)


@giveaway_bp.route('/edit_giveaway/<int:giveaway_id>', methods=['GET', 'POST'])
@login_required
def edit_giveaway(giveaway_id):
    giveaway = Giveaway.query.get_or_404(giveaway_id)
    if giveaway.creator_id != current_user.id:
        flash('You do not have permission to edit this giveaway.', 'error')
        return redirect(url_for('account.usergiveaways'))
    
    if request.method == 'POST':
        # Update giveaway details
        giveaway.title = request.form['title']
        giveaway.description = request.form['description']
        giveaway.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        # Add more fields as necessary
        
        db.session.commit()
        flash('Giveaway updated successfully.', 'success')
        return redirect(url_for('account.usergiveaways'))
    
    return render_template('edit_giveaway.html', giveaway=giveaway)


@giveaway_bp.route('/delete_giveaway/<int:giveaway_id>', methods=['POST'])
@login_required
def delete_giveaway(giveaway_id):
    giveaway = Giveaway.query.get_or_404(giveaway_id)
    
    # Check if the current user is the creator of the giveaway
    if current_user.id != giveaway.creator_id:
        flash('You do not have permission to delete this giveaway.', 'error')
        return redirect(url_for('account.usergiveaways'))
    
    # Delete the giveaway from the database
    db.session.delete(giveaway)
    db.session.commit()
    
    flash('Giveaway deleted successfully.', 'success')
    return redirect(url_for('account.usergiveaways'))