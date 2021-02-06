from flask import Blueprint, render_template, request
from flask_login import login_required, current_user
from project.models import Movies, User

compare_blueprint = Blueprint(
    'compare',
    __name__,
    template_folder='templates'
)

@compare_blueprint.route('/', methods=["GET"])
@login_required
def index():
    print(request.args.get('users'))

    user_movies = Movies.query.filter_by(user_id=current_user.id).all()
    user = User.query.filter_by(username=request.args.get('users')).first()
    other_movies = Movies.query.filter_by(user_id=user.id).all()


    for user_movie in user_movies:
        print(user_movie.movie_id)
    for other_movie in other_movies:
        print(other_movie.movie_id)

    return render_template('compare.html', movies = 0)