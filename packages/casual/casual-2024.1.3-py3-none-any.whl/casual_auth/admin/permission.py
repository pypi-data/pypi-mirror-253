from flask.templating import render_template
from flask_babel import lazy_gettext as _
from flask_menu import register_menu

from casual import db
from casual_auth.decorators import permission_required
from casual_auth.models import Permission

from ..blueprints import admin as bp


@bp.route("/permission/")
@register_menu(
    bp,
    ".admin.auth.permission",
    _("Permissions"),
    order=30,
    icon="box",
)
@permission_required
def permission_list():
    query = Permission.select()
    permissions = db.session.scalars(query)
    return render_template(
        "auth/admin.permission.list.html.j2",
        permissions=permissions,
    )
