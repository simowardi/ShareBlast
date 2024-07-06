from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import User
from models import db
from werkzeug.security import generate_password_hash

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    This function is responsible for handling the login process.
    It checks if the request method is 'POST',
    indicating that the login form has been submitted.
    If so, it retrieves the username and password from 
    the form data and queries the database for a user with the given username.
    If a user is found and the password matches,
    the user's ID is stored in the session and the user is redirected to the account page.
    Otherwise, an error message is displayed on the login page.

    Parameters:
    - None

    Returns:
    - If the request method is 'POST' and the login is successful, it redirects to the account page.
    - If the request method is 'POST' and the login is unsuccessful, it renders the login page with an error message.
    - If the request method is not 'POST', it renders the login page.
    """
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
            return redirect(url_for('account.account'))
        else:
            return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    This function is responsible for handling the registration process
    when a user submits the registration form. 
    It checks if the request method is 'POST', 
    indicating that the registration form has been submitted. 
    If so, it retrieves the username, email, and password from the form data 
    and creates a new user object with the provided information. 
    The new user object is then added to the database session and committed.
    the user's ID is stored in the session for future use.
    After successful registration, the user is redirected to the account page.

    Parameters:
    - None

    Returns:
    - If the request method is 'POST' and the registration is successful, it redirects to the account page.
    - If the request method is not 'POST', it renders the 'signup.html' template for the registration form.
    """
    if request.method == 'POST':
        # Handle registration logic
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

		# Check if user already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return render_template('signup.html', error="Email already registered")

		hashed_password = generate_password_hash(password)
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        # Optionally, set session or login user directly after registration
        session['user_id'] = new_user.id

        # Redirect to account page after registration
        return redirect(url_for('account.account'))

    return render_template('signup.html')


@auth_bp.route('/logout')
def logout():
    """
    Clears the session and redirects to the home page or login page.
    """
    # Clear the session
    session.clear()
    # Redirect to home page or login page
    return redirect(url_for('index'))
