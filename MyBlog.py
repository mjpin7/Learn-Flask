from app import app, db
from app.models import User, Post

# Creates a shell context for using the "flask shell" command. Mainly for testing in interpereter
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}