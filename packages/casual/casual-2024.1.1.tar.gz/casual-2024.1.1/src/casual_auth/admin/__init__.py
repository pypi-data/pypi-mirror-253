from flask import render_template
from flask_babel import lazy_gettext as _
from flask_menu import register_menu

from ..blueprints import admin as bp
from . import permission, role, user  # noqa


@bp.route("/")
@register_menu(
    bp,
    ".admin.auth",
    _("Authentication"),
    order=10,
    icon="lock",
)
def main():
    return render_template("admin.base.html.j2")
