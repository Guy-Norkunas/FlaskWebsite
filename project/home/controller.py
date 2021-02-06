from flask import Blueprint, render_template
from flask_login import current_user
import requests

home_blueprint = Blueprint(
    'home',
    __name__,
    template_folder='templates'
)

@home_blueprint.route('/', methods=["GET"])
def index():
    r = requests.get('https://api.github.com/events')
    print(r.text)
    return render_template('home.html')