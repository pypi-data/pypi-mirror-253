from flask import Blueprint

from casual_auth.decorators import check_permission

routes = Blueprint(
    "auth",
    __name__,
    url_prefix="/auth",
    template_folder="templates",
    static_folder="static",
)

admin = Blueprint(
    "admin_auth",
    __name__,
    url_prefix="/admin/auth",
    template_folder="templates",
    static_folder="static",
)

api_v1 = Blueprint(
    "api_auth",
    __name__,
    url_prefix="/api/v1/auth",
)


@admin.before_request
@check_permission
def before_request():
    pass
