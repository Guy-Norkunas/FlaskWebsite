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

    user_movies = Movies.query.filter_by(user_id=current_user).all()
    user = User.query.filter_by(username=request.args.get('users')).first()
    other_movies = Movies.query.filter_by(user_id=user).all()

    print(user_movies)
    print(other_movies)

    return render_template('compare.html', movies = )