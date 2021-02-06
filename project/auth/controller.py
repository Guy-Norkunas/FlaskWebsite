from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from project.models import User
from project import db


auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='templates'
)   

## login routes

# get

@auth_blueprint.route('/login', methods=["GET"])
def login_get():
    return render_template('login.html')

# post

@auth_blueprint.route('/login', methods=["POST"])
def login_post():
    return redirect(url_for('home.index'))

## signup routes

# get

@auth_blueprint.route('/signup', methods=["GET"])
def signup_get():
    return render_template('signup.html')

# post

@auth_blueprint.route('/signup', methods=["POST"])
def signup_post():
    username = request.form.get('username')
    password = request.form.get('password')

    # check if the username is already taken

    if User.query.filter_by(username=username).first():
        flash('Username is already taken')
        return redirect(url_for('auth.signup_get'))
    else:
        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        flash(f'Account creation successful, logged in as {username}')
        return redirect(url_for('home.index'))

# logout route

@auth_blueprint.route('/logout', methods=["DELETE"])
def logout():
    return render_template('logout.html')