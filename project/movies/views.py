from flask import Blueprint, render_template

movies_blueprint = Blueprint(
    'movies',
    __name__,
    template_folder='templates'
)   

@movies_blueprint.route('/<id>', methods=["GET"])
def movie(id):
    return render_template('movie.html', movie=f"movie {id}")
