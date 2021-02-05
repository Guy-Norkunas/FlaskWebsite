from flask import Blueprint, render_template
from project.models import User

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)   

@users_blueprint.route('/', methods=["GET", "POST"])
def self():
    return render_template('user.html', users=User.query.all())

@users_blueprint.route('/<id>', methods=["GET", "POST"])
def other(id):
    return render_template('user.html', users=User.query.get(id))