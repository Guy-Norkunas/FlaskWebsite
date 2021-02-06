from flask import Blueprint, render_template
from flask_login import current_user, login_required
from project.models import User

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)   

@users_blueprint.route('/', methods=["GET"])
@login_required
def self():
    return render_template('user.html', user=User.query.get(current_user.id))

@users_blueprint.route('/<id>', methods=["GET"])
@login_required
def other(id):
    return render_template('user.html', user=User.query.get(id))