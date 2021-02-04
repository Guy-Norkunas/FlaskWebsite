from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_modus import Modus
from flask_migrate import Migrate

app = Flask(__name__)
modus = Modus(app)

from project.users.views import users_blueprint

app.register_blueprint(users_blueprint, url_prefix='/user')

@app.route('/')
def root():
    return "Hello there."