from flask.templating import render_template
from flask_babel import lazy_gettext as _
from flask_menu import current_menu, register_menu

from casual_main.models import Notification

from .blueprint import route_blueprint as bp


@bp.route("/")
@register_menu(
    bp,
    ".main",
    _("Notifications"),
    icon="card-heading",
    order=0,
    visible_when=lambda: False,
)
def index():
    notifications = Notification.list()
    return render_template(
        "main/routes.index.html.j2",
        notifications=notifications,
    )


@bp.route("/about/")
@register_menu(
    bp,
    ".about",
    _("About Casual"),
    order=0,
    visible_when=lambda: False,
    icon="info-square",
)
def about():
    return render_template("admin.base.html.j2")
