from flask import abort, current_app, redirect, request
from flask.helpers import flash, url_for
from flask.templating import render_template
from flask_babel import lazy_gettext as _
from flask_login import current_user as cu
from flask_menu import register_menu

from casual import db
from casual_auth.decorators import permission_required
from casual_auth.forms import (
    AdminRoleCreateForm,
    AdminRoleForm,
    AdminUserRoleForm,
)
from casual_auth.models import Permission, Role, User
from casual_auth.signals import role_changed, role_created, role_deleted

from ..blueprints import admin as bp


@bp.route("/role/")
@register_menu(
    bp,
    ".admin.auth.role",
    _("Roles"),
    order=20,
    icon="boxes",
)
@permission_required
def role_list():
    query = Role.select().order_by(Role.name.asc())

    role_list = db.session.scalars(query)

    return render_template(
        "auth/admin.role.list.html.j2",
        role_list=role_list,
    )


@bp.route("/role/create/", methods=["GET", "POST"])
@permission_required
@register_menu(
    bp,
    ".admin.auth.role.create",
    _("Create Role"),
    order=10,
    # type="primary",
    icon="plus-square",
    visible_when=lambda: False,
    pagemenu=lambda: True,
)
def role_create():
    permissions = db.session.scalars(Permission.select())
    form = AdminRoleCreateForm()
    if form.validate_on_submit():
        role = Role()
        form.populate_obj(role)
        role.update_permissions(request.form.getlist("permissions"))
        role.update()
        role_created.send(current_app._get_current_object(), role=role)

        flash(_("Role %(name)s has been created.", name=(role.name)), "success")
        return redirect(url_for("admin_auth.role_list"))
    return render_template(
        "auth/admin.role.edit.html.j2",
        form=form,
        permissions=permissions,
    )


@bp.route("/role/<name>/")
@permission_required
@register_menu(
    bp,
    ".admin.auth.role.read",
    _("View"),
    order=20,
    type="primary",
    icon="eye",
    visible_when=lambda: False,
    endpoint_arguments_constructor=lambda: dict(name="role"),
    itemmenu=lambda: True,
)
def role_read(name):
    qry = Role.select().filter_by(name=name)
    role = db.session.scalar(qry) or abort(404)

    return render_template("auth/admin.role.read.html.j2", role=role)


@bp.route("/role/<name>/edit/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".admin.auth.role.edit",
    _("Edit"),
    order=30,
    type="secondary",
    icon="pencil",
    visible_when=lambda: False,
    endpoint_arguments_constructor=lambda: dict(name="role"),
    itemmenu=lambda: cu.hp(),
)
def role_edit(name):
    role = db.session.scalar(Role.select().filter_by(name=name)) or abort(404)
    permissions = db.session.scalars(Permission.select())
    form = AdminRoleForm(obj=role)

    if form.validate_on_submit():
        form.populate_obj(role)
        role.update_permissions(request.form.getlist("permissions"))
        role.update()
        role_changed.send(current_app._get_current_object(), role=role)

        flash(_("Role updated."), "success")

        return redirect(url_for("admin_auth.role_list"))

    return render_template(
        "auth/admin.role.edit.html.j2",
        form=form,
        role=role,
        permissions=permissions,
    )


@bp.route("/role/<name>/delete/")
@register_menu(
    bp,
    ".admin.auth.role.delete",
    _("Delete"),
    order=80,
    type="danger",
    icon="trash",
    visible_when=lambda: False,
    endpoint_arguments_constructor=lambda: dict(name="role"),
    itemmenu=lambda: True,
)
def role_delete(name):
    role_query = Role.select().filter_by(name=name)
    role = db.session.scalar(role_query) or abort(404)

    if role.users.count():
        flash(_("Role has users assigned. You cannot delete it."), "danger")
        return redirect(url_for("admin_auth.role_list"))
    role.delete()

    role_deleted.send(current_app._get_current_object(), role=role)

    flash(_("Role {name} has been deleted.".format(name=(name))), "success")
    return redirect(url_for("admin_auth.role_list"))


@bp.route("/role/<name>/users/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".admin.auth.role.users",
    _("Users"),
    order=50,
    type="secondary",
    icon="person",
    visible_when=lambda: False,
    endpoint_arguments_constructor=lambda: dict(name="role"),
    itemmenu=lambda: cu.hp(),
)
def role_users(name):
    role = db.session.scalar(Role.select().filter_by(name=name)) or abort(404)
    users_query = User.select()
    form = AdminUserRoleForm()

    # Filter out all app admins
    for admin in current_app.config["CASUAL_ADMINS"]:
        users_query = users_query.filter(User.email != admin)

    users = db.session.scalars(users_query)

    if form.validate_on_submit():
        selected_users = request.form.getlist("users")
        role.update_users(selected_users)
        role.update()
        flash(_("Roles updated for the selected users."), "success")
        return redirect(url_for("admin_auth.role_list"))

    return render_template(
        "auth/admin.role.users.html.j2",
        form=form,
        users=users,
        role=role,
    )
