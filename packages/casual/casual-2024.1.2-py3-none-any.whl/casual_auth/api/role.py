from apifairy import authenticate, body, other_responses, response
from casual_auth.models import Role
from casual_auth.schemas.role import (
    RolePermissionsEditSchema,
    RolePermissionsSchema,
    RoleSchema,
    RoleUsersSchema,
)
from flask import abort

from ..blueprints import api_v1


@api_v1.route("/role", methods=["GET"])
@response(RoleSchema(many=True))
def role_list():
    """Role List"""
    return Role.query.all()


@api_v1.route("/role", methods=["POST"])
@body(RoleSchema)
@response(RoleSchema, 201, "Role created")
@other_responses({409: "A role with the same name already exitst"})
def role_create(role):
    """Role Create"""
    if Role.query.filter_by(name=role.name).first():
        abort(409, "A role with the same name already exitst")

    role.update()

    return role, 201


@api_v1.route("/role/<int:id>", methods=["GET"])
@response(RoleSchema)
@other_responses({404: "Not Found"})
def role_read(id):
    """Role Read"""
    return Role.query.get_or_404(id)


@api_v1.route("/role", methods=["PUT"])
@body(RoleSchema)
@response(RoleSchema)
@other_responses({404: "Not Found"})
def role_edit(role):
    """Role Edit"""
    Role.query.get_or_404(role.id)
    role.update()
    return role


@api_v1.route("/role/permissions", methods=["POST"])
@body(RolePermissionsEditSchema)
@response(RolePermissionsEditSchema)
@other_responses({404: "Not Found"})
def role_edit_permissions(body):
    """Role Edit Permissions"""
    role = Role.query.get_or_404(body.get("id"))
    role.update_permissions(body.get("permissions", []))
    return role


@api_v1.route("/role/<int:id>", methods=["DELETE"])
@response(RoleSchema, 204)
def role_delete(id):
    """Role Delete"""
    role = Role.query.get_or_404(id)
    role.delete()
    return role, 204


@api_v1.route("/role/<int:id>/users", methods=["GET"])
@response(RoleUsersSchema)
def role_users(id):
    """Role List"""
    return Role.query.get_or_404(id)


@api_v1.route("/role/<int:id>/permissions", methods=["GET"])
@response(RolePermissionsSchema)
def role_permissions(id):
    """Role List"""
    return Role.query.get_or_404(id)
