from casual import ma
from casual_auth.models import User


_links = ma.Hyperlinks(
    {
        "self": ma.URLFor("api_auth.user_read", values=dict(id="<id>")),
        "roles": ma.URLFor("api_auth.user_roles", values=dict(id="<id>")),
        "permissions": ma.URLFor("api_auth.user_permissions", values=dict(id="<id>")),
        "collection": ma.URLFor("api_auth.user_list"),
    }
)

roles = ma.Function(lambda user: list(user.roles))
permissions = ma.Function(lambda user: list(user.permissions))

fields = [
    "active",
    "confirmed",
    "email",
    "failed_attempts",
    "force_pwd_change",
    "id",
    "is_admin",
    "locale",
    "location",
    "name",
    "password",
    "type",
    "username",
    "_links",
    "roles",
    "permissions",
]


class UserSchema(ma.SQLAlchemyAutoSchema):
    _links = _links
    roles = roles

    class Meta:
        model = User
        include_fk = True
        load_instance = True

        fields = fields.copy()
        fields.remove("permissions")


class UserEditSchema(UserSchema):
    username = ma.auto_field(dump_only=True)


class UserSelfSchema(ma.SQLAlchemyAutoSchema):
    roles = roles
    permissions = permissions

    class Meta:
        model = User
        include_fk = True
        load_instance = True

        fields = fields.copy()


class UserFilterSchema(ma.Schema):
    active = ma.Bool()
    confirmed = ma.Bool()
    email = ma.Str()
    failed_attempts = ma.Bool()
    force_pwd_change = ma.Bool()
    locale = ma.Str()
    name = ma.Str()
    username = ma.Str()


class UserIdSchema(ma.SQLAlchemySchema):
    id = ma.Int(required=True)

    class Meta:
        model = User
        load_instance = True


class UserRolesSchema(ma.SQLAlchemyAutoSchema):
    roles = ma.Function(lambda user: list(role.name for role in user._roles))

    class Meta:
        model = User
        load_instance = True

        fields = ["roles"]


class UserPermissionsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = User
        load_instance = True

        fields = ["permissions"]


class UserRolesEditSchema(ma.Schema):
    id = ma.Int(required=True)
    roles = ma.List(ma.Str(), required=True)

    class Meta:
        fields = ["roles", "id"]
