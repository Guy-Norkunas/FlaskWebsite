from flask import Blueprint, render_template

auth_blueprint = Blueprint(
    'auth',
    __name__,
    template_folder='templates'
)   

@auth_blueprint.route('/login', methods=["GET"])
def login():
    return render_template('login.html')

@auth_blueprint.route('/logout', methods=["GET"])
def logout():
    return render_template('logout.html')

@auth_blueprint.route('/signup', methods=["GET"])
def signup():
    return render_template('signup.html')