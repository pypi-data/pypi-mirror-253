from flask import current_app
from flask.helpers import flash, url_for
from flask.templating import render_template
from flask_babel import lazy_gettext as _
from flask_login import current_user as cu
from flask_menu import register_menu
from werkzeug.utils import redirect

from casual import db
from casual_auth.models import Permission

from .blueprints import admin_blueprint as bp


def _all_endpoints():
    result = [
        rule.endpoint
        for rule in current_app.url_map.iter_rules()
        if not rule.endpoint.endswith("static")
    ]
    return result


def _add_permissions(permissions=[]):
    for permission in permissions:
        query = Permission.select().filter_by(name=permission)

        if db.session.scalar(query) is None:
            new_permission = Permission(name=permission)
            new_permission.save()


def _remove_permissions(permissions=[]):
    for name in permissions:
        query = Permission.select().filter_by(name=name)
        permission = db.session.scalar(query)

        if permission is not None:
            if not permission.roles:
                permission.delete()


@bp.route("/")
@register_menu(
    bp,
    ".admin.basis",
    _("Basis"),
    order=999,
    icon="gear",
)
def main():
    _all_endpoints()

    return render_template("admin.base.html.j2")


@bp.route("/app/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".admin.basis.apps",
    _("Casual Apps"),
    visible_when=lambda: cu.hp(),
    order=10,
    icon="layout-wtf",
)
def list():
    casual_apps = current_app.casual_apps

    return render_template(
        "basis/admin.apps.list.html.j2",
        casual_apps=casual_apps,
    )


@bp.route("/app/install/", methods=["GET"])
@register_menu(
    bp,
    ".admin.basis.apps.install",
    _("Install Permissions"),
    visible_when=lambda: False,
    pagemenu=lambda: True,
    order=20,
    icon="menu-app",
)
def install():
    _add_permissions(permissions=_all_endpoints())

    flash(_("Permissions installed"), "success")

    return redirect(url_for("admin_basis.list"))


@bp.route("/app/uninstall/", methods=["GET"])
@register_menu(
    bp,
    ".admin.basis.apps.uninstall",
    _("Uninstall Permissions"),
    visible_when=lambda: False,
    pagemenu=lambda: True,
    order=20,
    # design='info',
    icon="menu-app",
)
def uninstall():
    _remove_permissions(permissions=_all_endpoints())

    flash(_("Permissions uninstalled"), "success")

    return redirect(url_for("admin_basis.list"))
