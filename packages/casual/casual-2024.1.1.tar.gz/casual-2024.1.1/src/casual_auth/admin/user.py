from flask import abort, current_app, redirect, request
from flask.helpers import flash, url_for
from flask.templating import render_template
from flask_babel import lazy_gettext as _
from flask_login import current_user as cu
from flask_menu import register_menu

from casual import db
from casual_auth.emails import user_new_email
from casual_auth.forms import (
    AdminUserCreateForm,
    AdminUserEditForm,
    AdminUserRoleForm,
)
from casual_auth.models import Role, User
from casual_auth.password import password_generator
from casual_auth.signals import user_changed

from ..blueprints import admin as bp


@bp.route("/user/")
@register_menu(
    bp,
    ".admin.auth.user",
    _("Users"),
    order=10,
    icon="people",
)
def user_list():
    query = User.select().order_by(User.id.asc())

    userlist = db.session.scalars(query)

    return render_template(
        "auth/admin.user.list_old.html.j2",
        userlist=userlist,
    )


@bp.route("/user/create/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".admin.auth.user.create",
    _("Create User"),
    order=10,
    icon="person-plus",
    visible_when=lambda: False,
    pagemenu=lambda: True,
)
def user_create():
    form = AdminUserCreateForm()
    form.locale.data = current_app.config["CASUAL_DEFAULT_LOCALE"]
    form.locale.choices = current_app.config["CASUAL_LANGUAGES"]

    if form.validate_on_submit():
        password = password_generator()

        user = User()
        form.populate_obj(user)

        user.password = password
        user.confirmed = True
        user.force_pwd_change = True

        if user.save():
            user_new_email(user, password)

            flash(
                _("User %(name)s has been created.", name=(user.name)),
                "success",
            )
            return redirect(url_for("admin_auth.user_list"))

    return render_template("auth/admin.user.edit.html.j2", form=form)


@bp.route("/user/<username>/")
@register_menu(
    bp,
    ".admin.auth.user.read",
    _("View"),
    order=20,
    type="primary",
    icon="eye",
    visible_when=lambda: False,
    endpoint_arguments_constructor=lambda: dict(username="user"),
    itemmenu=lambda: True,
)
def user_read(username):
    user = User.read(username)

    return render_template(
        "auth/admin.user.read.html.j2",
        user=user,
    )


@bp.route("/user/<username>/edit/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".admin.auth.user.edit",
    _("Edit"),
    order=30,
    type="secondary",
    icon="pencil",
    visible_when=lambda: False,
    endpoint_arguments_constructor=lambda: dict(username="user"),
    itemmenu=lambda: True,
)
def user_edit(username):
    query = User.select().where(User.username == username)
    user = db.session.scalar(query)

    if user.is_admin:
        flash(_("You are not allowed to edit the DDIC user."), "danger")
        return redirect(url_for("admin_auth.user_list"))
    if user is None:
        flash(
            _(
                "Username and Email for %(username)s already modified.",
                username=(username),
            ),
            "danger",
        )
        return redirect(url_for("admin_auth.user_list"))

    form = AdminUserEditForm(obj=user)

    form.username.render_kw = {
        "readonly": True,
        "disabled": True,
    }
    form.locale.choices = current_app.config["CASUAL_LANGUAGES"]

    if form.validate_on_submit():
        if form.username.data != user.username:
            abort(403, "You are not authorized to change the username!")
        form.username.data = user.username

        form.populate_obj(user)

        user.update()

        user_changed.send(
            current_app._get_current_object(),
            user=user,
        )

        flash(_("User %(name)s has been updated.", name=(user.name)), "success")

        return redirect(url_for("admin_auth.user_list"))

    return render_template(
        "auth/admin.user.edit.html.j2",
        form=form,
        user=user,
    )


@bp.route("/user/<username>/roles/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".admin.auth.user.roles",
    _("Roles"),
    order=50,
    type="secondary",
    icon="stickies",
    visible_when=lambda: False,
    endpoint_arguments_constructor=lambda: dict(username="user"),
    itemmenu=lambda: True,
)
def user_roles(username):
    user = User.read(username)
    if user.is_admin:
        flash(_("You are not allowed to edit administrators."), "danger")
        return redirect(url_for("admin_auth.user_list"))

    available_roles = db.session.scalars(Role.select())
    form = AdminUserRoleForm()

    if form.validate_on_submit():
        user.update_roles(request.form.getlist("roles"))
        user.update()
        flash(
            _("Roles for %(name)s have been updated.", name=(user.name)),
            "success",
        )
        return redirect(url_for("admin_auth.user_list"))

    return render_template(
        "auth/admin.user.roles.html.j2",
        form=form,
        user=user,
        roles=available_roles,
    )


@bp.route("/user/<username>/delete/")
@register_menu(
    bp,
    ".admin.auth.user.delete",
    _("Delete"),
    order=80,
    type="danger",
    icon="trash",
    visible_when=lambda: False,
    endpoint_arguments_constructor=lambda: dict(username="user"),
    itemmenu=lambda: True,
)
def user_delete(username):
    if cu.username == username:
        flash(_("You are not allowed to delete your own user!"), "danger")
        return redirect(request.referrer or url_for("admin_auth.user_list"))

    query = User.select().filter_by(username=username)

    user = db.session.scalar(query)

    if user.is_admin:
        flash(_("You are not allowed to edit the DDIC user."), "danger")
        return redirect(url_for("admin_auth.user_list"))

    if user is None:
        current_app.logger.error("%s failed to delete %s", cu.username, username)
        flash(_("User %(username)s does not exist.", username=(username)), "error")
    else:
        user.delete()
        flash(_("User %(name)s has been deleted.", name=(username)), "success")
    return redirect(url_for("admin_auth.user_list"))


@bp.route("/user/<id>/reset/failed/logins/")
def user_reset_failed_logins(id):
    user = User.read(id) or abort(404)
    user.failed_attempts = 0
    user.update()
    flash(
        _(
            "Failed login attepts for user %(name)s has been reset",
            name=(user.name),
        ),
        "success",
    )
    return redirect(url_for("admin_auth.user_list"))
