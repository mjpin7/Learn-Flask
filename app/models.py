from app import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

# Class containing the initial db schema for User
class User(UserMixin, db.Model):
    
    # This is the schema for the User table
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # Method to tell how to print the objects of this class
    def __repr__(self):
        return '<User {}>'.format(self.username)

    # Function to set the password hash based on the inputted password
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    # Function to check the password hash against the password
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    # Function that returns an avatar to the user
    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

# Class containing the initial db schema for a Post
class Post(db.Model):

    # This is the schema for the Post table
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.body)

# User loader function. Returns the user of a given id
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
