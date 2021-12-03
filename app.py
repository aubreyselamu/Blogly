"""Blogly application."""

from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, connect_db, User


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///blogly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# @app.route('/')
# def list_users():
#     """Redirect: List pets and show add form."""

#     return render_template('base.html')

@app.route('/users')
def show_users():
    '''Show all users'''

    users = User.query.order_by(User.last_name, User.first_name)
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods = ["GET"])
def add_user():
    '''Show an add form for users'''

    return render_template('users/new.html')

@app.route('/users/new', methods = ["POST"])
def add_user():
    '''Processing add form, adding a new user and going back to /users'''

    first_name = request.form["first_name"]
    last_name = request.form["last_name"]
    image_url = request.form["image_url"] or None

    new_user = User(first_name = first_name, last_name = last_name, image_url = image_url)

    db.session.add(new_user)
    db.session.commit()

    return redirect('/users')


