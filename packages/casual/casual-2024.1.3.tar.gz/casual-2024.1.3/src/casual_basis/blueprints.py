from casual_auth.decorators import check_permission
from flask import Blueprint

routes_blueprint = Blueprint(
    "basis",
    __name__,
    url_prefix="/basis",
    template_folder="templates",
    static_folder="static",
)

admin_blueprint = Blueprint(
    "admin_basis",
    __name__,
    url_prefix="/admin/basis",
    template_folder="templates",
    static_folder="static",
)


@admin_blueprint.before_request
@check_permission
def before_request():
    pass
