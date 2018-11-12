from flask import render_template
from app import app, db

# When a 404 "not found error" is found, execute this function
@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

# When a 500 "internal error" is found, execute this function
@app.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500