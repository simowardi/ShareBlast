from flask import Blueprint, request, render_template, redirect, url_for, flash
from models import db
from models.winner import Winner
from models.giveaway import Giveaway
from models.participation import Participation
from datetime import datetime
from flask_login import login_required, current_user


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
         
    if datetime.utcnow() >= giveaway.end_date:
        winner = giveaway.select_winner()
    else:
        winner = None

    return render_template('giveaway.html', giveaway=giveaway, winner=winner, now=datetime.utcnow)


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
        flash(f'The winner is {winner.username}', 'success')
    else:
        flash('No participants found or giveaway not yet ended.', 'warning')

    return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway_id))


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


@giveaway_bp.route('/giveaway/<int:giveaway_id>/download/<file_format>', methods=['GET'])
@login_required
def download_leads(giveaway_id, file_format):
        """
            Download the leads for a giveaway in the specified file format.
                Args:
                        giveaway_id (int): The ID of the giveaway.
                                file_format (str): The format of the file to download the leads in ('txt' or 'csv').
                                    Returns:
                                            the downloaded leads in the specified file format.
                                                Raises:
                                                        flask.abort.NotFound: If the giveaway with the given ID does not exist.
                                                            Side Effects:
                                                                    Flashes a message if the user is not authorized to download the leads.
                                                                            Redirects to the view_giveaway page if the user is not authorized.
                                                                                    Flashes a message if an invalid file format is requested.
                                                                                            Redirects to the view_leads page if an invalid file format is requested.
                                                                                                """
                                                                                                    giveaway = Giveaway.query.get_or_404(giveaway_id)
                                                                                                        if current_user.id != giveaway.creator_id:
                                                                                                                    flash('You are not authorized to download the leads for this giveaway.', 'danger')
                                                                                                                            return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway_id))
                                                                                                                            
                                                                                                                            participations = Participation.query.filter_by(giveaway_id=giveaway_id).all()
                                                                                                                                leads = [(p.user.username, p.user.email) for p in participations]

                                                                                                                                    if file_format == 'txt':
                                                                                                                                                output = "\n".join([f"{username}, {email}" for username, email in leads])
                                                                                                                                                        response = make_response(output)
                                                                                                                                                                response.headers["Content-Disposition"] = f"attachment; filename=leads_{giveaway.id}.txt"
                                                                                                                                                                        response.headers["Content-Type"] = "text/plain"
                                                                                                                                                                            elif file_format == 'csv':
                                                                                                                                                                                        output = StringIO()
                                                                                                                                                                                                writer = csv.writer(output)
                                                                                                                                                                                                        writer.writerow(['Username', 'Email'])
                                                                                                                                                                                                                writer.writerows(leads)
                                                                                                                                                                                                                        response = make_response(output.getvalue())
                                                                                                                                                                                                                                response.headers["Content-Disposition"] = f"attachment; filename=leads_{giveaway.id}.csv"
                                                                                                                                                                                                                                        response.headers["Content-Type"] = "text/csv"
                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                        flash('Invalid file format requested.', 'danger')
                                                                                                                                                                                                                                                                return redirect(url_for('giveaway.view_leads', giveaway_id=giveaway_id))
                                                                                                                                                                                                                                                                
                                                                                                                                                                                                                                                                return response
