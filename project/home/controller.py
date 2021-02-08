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

    r = requests.get(f"https://api.themoviedb.org/3/discover/movie?api_key={os.environ.get('API_KEY')}&language=en-US&sort_by=popularity.desc&include_video=false&page=1")
    return render_template('home.html', movies=r.json()['results'][:10])