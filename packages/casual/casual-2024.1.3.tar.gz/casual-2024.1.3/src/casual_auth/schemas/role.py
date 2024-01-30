from casual import ma
from casual_auth.models import Role


class RoleSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Role
        include_fk = True
        load_instance = True

        fields = [
            "id",
            "name",
            "description",
            "group",
        ]


class RoleUsersSchema(ma.SQLAlchemyAutoSchema):
    # users = ma.Nested(UserSchema(many=True))
    users = ma.Function(
        lambda role: list(
            dict(
                username=user.username,
                name=user.name,
                id=user.id,
            )
            for user in role.users
        )
    )

    class Meta:
        model = Role
        include_fk = True
        load_instance = True

        fields = [
            "id",
            "name",
            "description",
            "group",
            "users",
        ]


class RolePermissionsSchema(ma.SQLAlchemyAutoSchema):
    permissions = ma.Function(
        lambda role: list(
            dict(
                name=permission.name,
                group=permission.group,
                id=permission.id,
            )
            for permission in role.permissions
        )
    )

    class Meta:
        model = Role
        include_fk = True
        load_instance = True

        fields = [
            "id",
            "name",
            "description",
            "group",
            "permissions",
        ]


class RolePermissionsEditSchema(ma.Schema):
    id = ma.Int(required=True)
    permissions = ma.List(ma.Str(), required=True)

    class Meta:
        fields = ["permissions", "id"]
