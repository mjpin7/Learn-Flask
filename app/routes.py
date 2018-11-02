from app import app, db
from flask import render_template, flash, redirect, url_for, request
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User
from werkzeug.urls import url_parse

# When on the paths '/' and '/index', run the index method. Login is required to view this
@app.route('/')
@app.route('/index')
@login_required
def index():
    posts = [
        {
            'author': {'username': 'susan'},
            'body': 'How do you do fellow kids'
        },
        {
            'author': {'username': 'Mary'},
            'body': 'YEEET'
        }
    ]
    return render_template('index.html', title="Home", posts=posts)

# When on the '/login' path, run the login method to render the login page to the browser
@app.route('/login', methods=['GET', 'POST'])
def login():
    # If the current user is already logged in, redirect to index
    if current_user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()

    # When the form is submitted
    if form.validate_on_submit():

        # Load the user from the database
        user = User.query.filter_by(username=form.username.data).first()

        # If there is no user existing with that username or it is an invalid password
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        
        # If the username and password are both correct, call the login function
        login_user(user, remember=form.remember_me.data)

        # Get the value of the next argument 
        next_page = request.args.get('next')

        # if the url does not have a next arg or parse the url to check if it is relative or absolute
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')

        return redirect(next_page)
    
    return render_template('login.html', title='Sign In', form=form)

# When the login button is clicked, log the user out and then redirect
@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

# When you go to registration link
@app.route('/register', methods=['GET', 'POST'])
def register():
    # Check if the user is logged in first
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    # Create the form
    form = RegistrationForm()

    # Execute when the form has been submitted
    if form.validate_on_submit():
        # Create the new user. Set the password and add the user to the database
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('New user registered!')
        return redirect(url_for('login'))
    
    return render_template('register.html', title="Register", form=form)
