from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user import User
from . import db

auth_bp = Blueprint('auth', __name__)


auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle login logic
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            session['user_id'] = user.id
                return redirect(url_for('account.html'))
        else:
                return render_template('login.html', error='Invalid username or password')

    return render_template('login.html')


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Handle registration logic
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        
        # Optionally, set session or login user directly after registration
        session['user_id'] = new_user.id

        # Redirect to account page after registration
        return redirect(url_for('account.html'))

    return render_template('signup.html')
