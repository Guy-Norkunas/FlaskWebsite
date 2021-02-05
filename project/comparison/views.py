from flask import Blueprint, render_template


compare_blueprint = Blueprint(
    'compare',
    __name__,
    template_folder='templates'
)

@compare_blueprint.route('/', methods=["GET"])
def index():
    return render_template('compare.html')