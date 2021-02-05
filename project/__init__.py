from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_migrate import Migrate
import os

# basic initialisation

app = Flask(__name__)

# database connection / config

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://guy:password@localhost/test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "test123"
db = SQLAlchemy(app)
db.init_app(app)

migrate = Migrate(app, db)

# method overides

modus = Modus(app)

# bluepring initialisations

from project.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/user')

# blueprint for auth routes

from project.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for non-auth routes

from project.home.views import home_blueprint
app.register_blueprint(home_blueprint, url_prefix='/home')


# root route

@app.route('/')
def root():
    return render_template('base.html')