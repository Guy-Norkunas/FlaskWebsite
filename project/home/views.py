from flask import Blueprint, render_template

home_blueprint = Blueprint(
    'home',
    __name__,
    template_folder='templates'
)   

@main.route('/')
def index():
    return 'Home'