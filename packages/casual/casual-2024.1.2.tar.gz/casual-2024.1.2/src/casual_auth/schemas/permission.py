from casual import ma
from casual_auth.models import Permission


class PermissionSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Permission
        fields = ["id", "name", "group"]
