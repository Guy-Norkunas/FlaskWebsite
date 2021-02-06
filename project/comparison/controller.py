from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from project.models import Movies, User
import requests


compare_blueprint = Blueprint(
    'compare',
    __name__,
    template_folder='templates'
)

@compare_blueprint.route('/', methods=["GET"])
@login_required
def index():
    movies = []

    if(request.args.get('users')):

        user_movies = Movies.query.filter_by(user_id=current_user.id).with_entities(Movies.movie_id).all()
        user = User.query.filter_by(username=request.args.get('users')).first()
        other_movies = Movies.query.filter_by(user_id=user.id).with_entities(Movies.movie_id).all()
        common_movies = list(set(user_movies) & set(other_movies))

        for common_movie in common_movies:

            r = requests.get(f"https://api.themoviedb.org/3/movie/{common_movie[0]}?api_key=cd082f86556318fbd6e151825ae40fc7&language=en-US")
            movies.append(r.json())

        return render_template('compare.html', movies = movies)

    else:
        return render_template('compare.html')