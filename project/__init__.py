from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
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

## blueprint initialisations

# blueprint for user pages

from project.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/user')

# blueprint for auth pages

from project.auth.views import auth_blueprint
app.register_blueprint(auth_blueprint)

# blueprint for home page

from project.home.views import home_blueprint
app.register_blueprint(home_blueprint, url_prefix='/home')

# blueprint for comparison page

from project.compare.views import compare_blueprint
app.register_blueprint(compare_blueprint, url_prefix='/compare')

# root route

@app.route('/')
def root():
    return render_template('base.html')