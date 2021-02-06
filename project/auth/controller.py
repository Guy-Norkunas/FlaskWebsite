from flask import Blueprint, render_template, redirect, url_for

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='templates'
)   

@auth_blueprint.route('/login', methods=["GET"])
def login_get():
    return render_template('login.html')

@auth_blueprint.route('/login', methods=["POST"])
def login_post():
    return redirect(url_for('home.index'))

@auth_blueprint.route('/logout', methods=["GET"])
def logout():
    return render_template('logout.html')

@auth_blueprint.route('/signup', methods=["GET"])
def signup_get():
    return render_template('signup.html')

@auth_blueprint.route('/signup', methods=["POST"])
def signup_post():
    return redirect(url_for('home.index'))