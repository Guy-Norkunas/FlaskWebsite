from flask import Blueprint, render_template, request
from flask_login import login_required, current_user


compare_blueprint = Blueprint(
    'compare',
    __name__,
    template_folder='templates'
)

@compare_blueprint.route('/', methods=["GET"])
@login_required
def index():
    print(request.args.get('users'))

    return render_template('compare.html')