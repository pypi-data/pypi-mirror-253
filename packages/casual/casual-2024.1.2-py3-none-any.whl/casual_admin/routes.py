from flask import render_template
from flask_babel import lazy_gettext as _
from flask_menu import register_menu

from casual_auth.decorators import permission_required

from .bp import bp


@bp.route("/")
@register_menu(
    bp,
    ".admin",
    _("Administration"),
    icon="tools",
    order=900,
)
@permission_required
def main():
    return render_template("admin.base.html.j2")
