from apifairy import arguments, body, other_responses, response
from flask_login import current_user

from casual_auth.decorators import permission_required
from casual_main.blueprint import v1

from .models import Notification
from .schemas import NotificationFilterSchema, NotificationSchema


@v1.route("/notification", methods=["POST"])
@permission_required
@body(NotificationSchema)
@response(NotificationSchema)
def main_notification_create(notification):
    """Add Notification"""
    notification.author_id = current_user.id
    notification.update()

    return notification, 201


@v1.route("/notification", methods=["GET"])
@permission_required
@arguments(NotificationFilterSchema)
@response(NotificationSchema(many=True))
def main_notification_list(filter):
    """Notification List

    `start_date` and `end_date` are not exact filter criteria.
    """
    if len(filter) == 0:
        return Notification.list()

    resources = Notification.query

    all = filter.get("all")

    if not all:
        id = filter.get("id")
        author_id = filter.get("author_id")
        locale = filter.get("locale")
        start_date = filter.get("start_date")
        end_date = filter.get("end_date")

        if id:
            resources = resources.filter_by(id=id)
        if author_id:
            resources = resources.filter_by(author_id=author_id)
        if locale:
            resources = resources.filter_by(locale=locale)
        if start_date:
            resources = resources.filter(Notification.start_date <= start_date)
        if end_date:
            resources = resources.filter(Notification.end_date >= end_date)

    resources = resources.all()

    return resources


@v1.route("/notification", methods=["PUT"])
@permission_required
@response(NotificationSchema)
@body(NotificationSchema)
def main_notification_update(notification):
    """Edit Notifications"""
    Notification.query.get_or_404(notification.id)

    notification.author_id = current_user.id
    notification.update()

    return notification


@v1.route("/notification/<int:id>", methods=["DELETE"])
@permission_required
@response(NotificationSchema, 204, "Deleted succesfuly")
@other_responses({404: "Not Found", 403: "Forbidden"})
def main_notification_delete(id):
    """Delete Notification"""
    notification = Notification.query.get_or_404(id)
    notification.delete()

    return "", 204
