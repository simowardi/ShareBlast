from flask import Blueprint, render_template, request, redirect, session, url_for
from models import db, Giveaway


giveaway_bp = Blueprint('giveaway', __name__)

@giveaway_bp.route('/create-giveaway', methods=['GET', 'POST'])
def create_giveaway():
    """
    Create a new giveaway.
    This function is a route handler for the '/create-giveaway' endpoint. It handles both GET and POST requests.
    Parameters:
        None
    Returns:
        If the request method is POST, the function creates a new giveaway with the provided data,
        If the request method is GET, the function renders the 'create_giveaway.html' template.
    Raises:
        None
    """
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        image_url = request.form['image_url']
        end_date = request.form['end_date']
        
		# Convert end_date to datetime object
        end_date = datetime.strptime(end_date, '%Y-%m-%dT%H:%M')

        new_giveaway = Giveaway(
            title=title,
            description=description,
            image_url=image_url,
            end_date=end_date,
            user_id=session['user_id']
        )

        db.session.add(new_giveaway)
        db.session.commit()

	    return render_template('giveaway_created.html', giveaway_id=new_giveaway.id)

    return render_template('create_giveaway.html')


@giveaway_bp.route('/giveaway/<int:giveaway_id>', methods=['GET'])
def view_giveaway(giveaway_id):
    """
    Retrieves a giveaway by ID and renders the 'giveaway.html' template with the giveaway data.
    Parameters:
        giveaway_id (int): The ID of the giveaway to retrieve.
    Returns:
    render_template: Renders the 'giveaway.html' template with the giveaway data.
    """
    giveaway = Giveaway.query.get_or_404(giveaway_id)
    return render_template('giveaway.html', giveaway=giveaway)


@giveaway_bp.route('/enter-giveaway/<int:giveaway_id>', methods=['POST'])
def enter_giveaway(giveaway_id):
	"""
	Check if the user is logged in
	Get the user ID from the session
	Check if the user has already entered the giveaway
	recording the user's entry
	"""
	# Check if the user is logged in
    if 'user_id' not in session:
        return redirect(url_for('auth.login'))

	# Get the user ID from the session
    user_id = session['user_id']
    giveaway = Giveaway.query.get_or_404(giveaway_id)

	# Check if the user has already entered the giveaway
	if user_id in giveaway.participants:
		return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway.id))

	giveaway.participants.append(user_id)
	db.session.commit()

    # Logic for entering the giveaway, e.g., recording the user's entry

    return redirect(url_for('giveaway.view_giveaway', giveaway_id=giveaway.id))