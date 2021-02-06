from flask import Blueprint, render_template, redirect, request
from flask_login import current_user, login_required
import requests

movies_blueprint = Blueprint(
    'movies',
    __name__,
    template_folder='templates'
)   

@movies_blueprint.route('/<id>', methods=["GET"])
def movie(id):

    r = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=cd082f86556318fbd6e151825ae40fc7&language=en-US")

    return render_template('movie.html', movie=r.json())

@movies_blueprint.route('/<id>', methods=["POST"])
@login_required
def favourite(id):
    print(request.args.get('url'))
    return redirect(request.args.get('url'))