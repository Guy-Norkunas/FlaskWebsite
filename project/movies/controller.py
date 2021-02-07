from flask import Blueprint, render_template, redirect, request
from flask_login import current_user, login_required
import requests
from project.models import Movies
from project import db

movies_blueprint = Blueprint(
    'movies',
    __name__,
    template_folder='templates'
)   

@movies_blueprint.route('/<id>', methods=["GET"])
def movie(id):

    r = requests.get(f"https://api.themoviedb.org/3/movie/{id}?api_key=cd082f86556318fbd6e151825ae40fc7&language=en-US")

    return render_template('movie.html', movie=r.json())

# favourite logic

@movies_blueprint.route('/<id>', methods=["POST"])
@login_required
def favourite(id):
    
    favourite = Movies.query.filter_by(user_id=current_user.id).filter_by(movie_id=id).first()

    if favourite:

        print("first condition")
        print(favourite.id)

        db.session.delete(favourite)
        db.session.commit()
        return redirect(request.args.get('url'))
    else:
        print("second condition")
        new_favourite = Movies(user_id=current_user.id, movie_id=id)
        db.session.add(new_favourite)
        db.session.commit()
        return redirect(request.args.get('url'))


@movies_blueprint.route('/<id>', methods=["GET"])
@login_required
def isFavourite(id):
    favourite = Movies.query.filter_by(user_id=current_user.id).filter_by(movie_id=id).first()
    if favourite:
        return "True"
    else:
        return "False"