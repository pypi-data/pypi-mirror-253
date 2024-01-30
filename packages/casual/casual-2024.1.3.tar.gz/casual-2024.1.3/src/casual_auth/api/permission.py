from apifairy import other_responses, response
from casual_auth.decorators import permission_required
from casual_auth.models import Permission
from casual_auth.schemas.permission import PermissionSchema

from ..blueprints import api_v1


@api_v1.route("/permission", methods=["GET"])
@permission_required
@response(PermissionSchema(many=True))
def permission_list():
    """Permission List"""
    return Permission.query.all()


@api_v1.route("/permission/<int:id>", methods=["GET"])
@permission_required
@response(PermissionSchema)
@other_responses({404: "Not Found"})
def permission_read(id):
    """Permission Read"""
    return Permission.query.get_or_404(id)
