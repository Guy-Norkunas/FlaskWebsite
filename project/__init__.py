from flask import Flask, render_template, url_for, redirect, get_flashed_messages
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, current_user
import os

# basic initialisation

print(os.environ)
print(os.environ.get('DATABASE_URI'))

app = Flask(__name__)

# database connection / config

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
db = SQLAlchemy(app)
db.init_app(app)
migrate = Migrate(app, db)

# login manager config

login_manager = LoginManager()
login_manager.login_view = 'auth.login_get'
login_manager.init_app(app)

from .models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

## blueprint initialisations

# blueprint for user pages

from project.users.controller import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/user')

# blueprint for auth pages

from project.auth.controller import auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for home page

from project.home.controller import home_blueprint
app.register_blueprint(home_blueprint, url_prefix='/home')

# blueprint for comparison page

from project.comparison.controller import compare_blueprint
app.register_blueprint(compare_blueprint, url_prefix='/compare')

# blueprint for movies page

from project.movies.controller import movies_blueprint
app.register_blueprint(movies_blueprint, url_prefix='/movie')

# root route

@app.route('/')
def root():
    get_flashed_messages()
    return render_template('base.html')