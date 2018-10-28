from app import app
from flask import render_template, flash, redirect
from app.forms import LoginForm

# When on the paths '/' and '/index', run the index method
@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'MJPIN1'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'How do you do fellow kids'
        },
        {
            'author': {'username': 'Mary'},
            'body': 'YEEET'
        }
    ]
    return render_template('index.html', title="Home", user=user, posts=posts)

# When on the '/login' path, run the login method to render the login page to the browser
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
        return redirect('/index')

    return render_template('login.html', title="Sign In", form=form)