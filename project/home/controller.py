from flask import Blueprint, render_template
from flask_login import current_user
import requests, json

home_blueprint = Blueprint(
    'home',
    __name__,
    template_folder='templates'
)

@home_blueprint.route('/', methods=["GET"])
def index():

    r = requests.get('https://api.themoviedb.org/3/discover/movie?api_key=cd082f86556318fbd6e151825ae40fc7&language=en-US&sort_by=popularity.desc&include_video=false&page=1')
    return render_template('home.html', movies=r.json()['results'][:10])