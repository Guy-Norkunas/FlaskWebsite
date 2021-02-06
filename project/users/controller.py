from flask import Blueprint, render_template
from flask_login import current_user, login_required
from project.models import User, Movies
import requests

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)   

@users_blueprint.route('/<id>', methods=["GET"])
@login_required
def index(id):
    print(id)
    movies = []

    user_movies = Movies.query.filter_by(user_id=current_user.id).with_entities(Movies.movie_id).all()
    for user_movie in user_movies:


        r = requests.get(f"https://api.themoviedb.org/3/movie/{user_movie[0]}?api_key=cd082f86556318fbd6e151825ae40fc7&language=en-US")
        movies.append(r.json())

    return render_template('user.html', user=User.query.get(id), movies = movies)