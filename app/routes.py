from app import app
from flask import render_template

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