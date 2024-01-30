from apifairy import arguments, body, other_responses, response
from casual_auth.models import User
from casual_auth.password import password_generator
from casual_auth.schemas.user import (
    UserEditSchema,
    UserFilterSchema,
    UserPermissionsSchema,
    UserRolesEditSchema,
    UserRolesSchema,
    UserSchema,
    UserSelfSchema,
)
from flask import abort
from flask_login import current_user

from ..blueprints import api_v1


@api_v1.route("/user", methods=["GET"])
@response(UserSchema(many=True))
def user_list():
    """User List"""
    return User.query.all()


@api_v1.route("/user/search", methods=["GET"])
@arguments(UserFilterSchema)
@response(UserSchema(many=True))
def user_search(filter):
    """User Search"""
    user_list = User.query

    active = filter.get("active")
    confirmed = filter.get("confirmed")
    email = filter.get("email")
    failed_attempts = filter.get("failed_attempts")
    force_pwd_change = filter.get("force_pwd_change")
    locale = filter.get("locale")
    name = filter.get("name")
    username = filter.get("username")

    # Failed login attempts are interesting if 0 or NOT 0
    if failed_attempts is not None:
        if failed_attempts:
            user_list = user_list.filter(User.failed_attempts != 0)
        else:
            user_list = user_list.filter(User.failed_attempts == 0)

    if active is not None:
        user_list = user_list.filter_by(active=active)

    if confirmed is not None:
        user_list = user_list.filter_by(confirmed=confirmed)

    if email is not None:
        user_list = user_list.filter_by(email=email)

    if force_pwd_change is not None:
        user_list = user_list.filter_by(force_pwd_change=force_pwd_change)

    if locale is not None:
        user_list = user_list.filter_by(locale=locale)

    if name is not None:
        user_list = user_list.filter(User.name.like(f"%{name}%"))

    if username is not None:
        user_list = user_list.filter(User.username.like(f"%{username}%"))

    return user_list.all()


@api_v1.route("/user", methods=["POST"])
@body(UserSchema)
@response(UserSchema, 201, "User created.")
@other_responses({409: "User already exists."})
def user_create(user):
    """User Create"""
    if User.query.filter_by(email=user.email).first():
        abort(409)

    if not user.password_hash:
        user.password = password_generator()

    user.confirmed = False
    user.force_pwd_change = True

    user.update()

    return user, 201


@api_v1.route("/user/<int:id>", methods=["GET"])
@response(UserSchema)
def user_read(id):
    """User Read"""
    return User.query.get_or_404(id)


@api_v1.route("/user", methods=["PUT"])
@body(UserEditSchema)
@response(UserSchema)
def user_edit(user):
    """User Edit"""
    User.query.get_or_404(user.id)

    user.update()
    return user


@api_v1.route("/user/roles", methods=["POST"])
@body(UserRolesEditSchema)
@response(UserRolesEditSchema)
@other_responses({404: "Not Found"})
def user_edit_roles(body):
    """User Edit Roles"""
    user = User.query.get_or_404(body.get("id"))
    user.update_roles(body.get("roles", []))
    return user


@api_v1.route("/user/<int:id>", methods=["DELETE"])
@response(UserSchema, 204, "Deleted succesfuly")
@other_responses(
    {
        403: "Cannot delete administrators or own account.",
        404: "Not Found",
    }
)
def user_delete(id):
    """User Delete"""
    user = User.query.get_or_404(id)

    if current_user.id == user.id or user.is_admin:
        abort(403, "Cannot delete administrators or own account.")

    user.delete()

    return user, 204


@api_v1.route("/user/self", methods=["GET"])
@response(UserSelfSchema)
def user_self():
    """User Self

    Returns the details corresponding to the provided Bearer Token."""
    return current_user


@api_v1.route("/user/<int:id>/roles", methods=["GET"])
@response(UserRolesSchema)
@other_responses({404: "Not Found"})
def user_roles(id):
    """User Roles"""
    return User.query.get_or_404(id)


@api_v1.route("/user/<int:id>/permissions", methods=["GET"])
@response(UserPermissionsSchema)
@other_responses({404: "Not Found"})
def user_permissions(id):
    """User Permissions"""
    return User.query.get_or_404(id)
