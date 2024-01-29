from casual_auth.decorators import check_permission
from flask import Blueprint

route_blueprint = Blueprint(
    "main",
    __name__,
    url_prefix="/",
    template_folder="templates",
    static_folder="static",
)


admin_blueprint = Blueprint(
    "admin_main",
    __name__,
    url_prefix="/admin/main",
    template_folder="templates",
    static_folder="static",
)


@admin_blueprint.before_request
@check_permission
def before_request():
    pass
