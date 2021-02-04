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

migrate = Migrate(app, db)

# method overides

modus = Modus(app)

# bluepring initialisation

from project.users.views import users_blueprint
app.register_blueprint(users_blueprint, url_prefix='/user')

# root route

@app.route('/')
def root():
    return render_template('base.html')