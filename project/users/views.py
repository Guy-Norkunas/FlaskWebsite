from flask import Blueprint
from project.models import User

users_blueprint = Blueprint(
    'users',
    __name__,
    template_folder='templates'
)