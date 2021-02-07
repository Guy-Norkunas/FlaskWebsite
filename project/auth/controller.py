from flask import Blueprint, render_template, redirect, url_for, request, flash, session
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from project.models import User
from project import db

print("start of controller")

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='templates'
)   

## login routes

print("after blueprint")

# get

@auth_blueprint.route('/login', methods=["GET"])
def login_get():

    print("start of login_get")

    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('home.index'))

    return render_template('login.html')

print("after /login GET route")

# post

@auth_blueprint.route('/login', methods=["POST"])
def login_post():

    print("start of login_post")

    if current_user.is_authenticated:

        print("user is authenticatded")

        flash('You are already logged in')
        return redirect(url_for('home.index'))

    print("before getting form stuff")

    username = request.form.get('username')
    password = request.form.get('password')

    print("after getting form stuff")

    user = User.query.filter_by(username=username).first()

    print("after doing a query")

    if user and check_password_hash(user.password, password):
        print("check username and pass successful")
        login_user(user)
        return redirect(url_for('home.index'))
    else:
        flash('Incorrect username or password')
        return redirect(url_for('auth.login_get'))


    return redirect(url_for('home.index'))

## signup routes

# get

@auth_blueprint.route('/signup', methods=["GET"])
def signup_get():

    print("signup_get")

    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('home.index'))

    return render_template('signup.html')

# post

@auth_blueprint.route('/signup', methods=["POST"])
def signup_post():

    print("signup_post")

    if current_user.is_authenticated:
        flash('You are already logged in')
        return redirect(url_for('home.index'))

    print("before form stuff")

    username = request.form.get('username')
    password = request.form.get('password')

    print("after form stuff")

    # check if the username is already taken

    if User.query.filter_by(username=username).first():

        print("username taken")

        flash('Username is already taken')
        return redirect(url_for('auth.signup_get'))
    else:

        print("registering new user")

        new_user = User(username=username, password=generate_password_hash(password, method='sha256'))
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash(f'Account creation successful, logged in as {username}')
        return redirect(url_for('home.index'))

# logout route

@auth_blueprint.route('/logout', methods=["GET"])
@login_required
def logout():
    logout_user()
    flash('Successfully logged out')
    return render_template('home.html')