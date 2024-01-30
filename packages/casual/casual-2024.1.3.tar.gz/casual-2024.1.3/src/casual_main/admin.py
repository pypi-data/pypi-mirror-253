from flask import abort, current_app, flash, redirect, render_template, url_for
from flask_babel import lazy_gettext as _
from flask_login import current_user as cu
from flask_menu import register_menu

from casual import db

from .blueprint import admin_blueprint as bp
from .forms import NotificationForm
from .models import Notification


@bp.route("/notification/")
@register_menu(
    bp,
    ".admin.notification",
    _("Notifications"),
    order=990,
    visible_when=lambda: True,
    icon="bell",
)
def notification_list():
    notifications = db.session.scalars(Notification.select())

    return render_template(
        "main/admin.notification.list.html.j2",
        notifications=notifications,
    )


@bp.route("/notification/create/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".admin.notification.create",
    _("Add Notification"),
    order=10,
    visible_when=lambda: False,
    icon="plus-square",
    type="light",
    pagemenu=lambda: True,
)
def notification_create():
    form = NotificationForm(locale=cu.locale)
    form.locale.choices = current_app.config["CASUAL_LANGUAGES"]
    form.submit.label.text = _("Create Notification")

    if form.validate_on_submit():
        notification = Notification()
        form.populate_obj(notification)
        notification.author = cu
        notification.save()
        flash(_("Notification created successfully."), "success")
        return redirect(url_for("admin_main.notification_list"))

    return render_template("main/admin.notification.edit.html.j2", form=form)


@bp.route("/notification/<int:id>/edit/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".admin.notification.edit",
    _("Edit"),
    order=30,
    visible_when=lambda: False,
    icon="pen",
    type="secondary",
    endpoint_arguments_constructor=lambda: dict(id=1),
    itemmenu=lambda: True,
)
def notification_edit(id):
    notification = db.session.scalar(Notification.select().where(Notification.id == id)) or abort(404)

    form = NotificationForm(obj=notification)
    form.locale.choices = current_app.config["CASUAL_LANGUAGES"]
    form.submit.label.text = _("Update Notification")

    if form.validate_on_submit():
        notification.author = cu
        form.populate_obj(notification)
        notification.update()
        flash(_("Notification updated sucessfuly"), "success")
        return redirect(url_for("admin_main.notification_list"))
    return render_template("main/admin.notification.edit.html.j2", form=form)


@bp.route("/notification/<int:id>/delete/")
@register_menu(
    bp,
    ".admin.notification.delete",
    _("Delete"),
    order=40,
    visible_when=lambda: False,
    icon="trash",
    type="danger",
    endpoint_arguments_constructor=lambda: dict(id=1),
    itemmenu=lambda: True,
)
def notification_delete(id):
    notification = Notification.read(id) or abort(404)
    notification.delete()
    return redirect(url_for("admin_main.notification_list"))


@bp.route("/notification/clean/")
@register_menu(
    bp,
    ".admin.notification.clean",
    _("Clean"),
    order=50,
    visible_when=lambda: False,
    icon="bell-slash",
    type="light",
    pagemenu=lambda: True,
)
def notification_clean():
    counter = Notification.clean_up()

    flash(_("%(counter)s notifications have been removed.", counter=counter))

    current_app.logger.info("Notification cleanup started...")

    return redirect(url_for("admin_main.notification_list"))
