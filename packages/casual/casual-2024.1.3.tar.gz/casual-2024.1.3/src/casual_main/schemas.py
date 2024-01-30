from datetime import date

from casual import ma

from casual_main.models import Notification


class NotificationSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Notification
        include_fk = True
        load_instance = True

        fields = [
            "id",
            "body",
            "body_html",
            "author_id",
            "locale",
            "start_date",
            "end_date",
        ]


class NotificationFilterSchema(ma.Schema):
    all = ma.Bool()
    id = ma.Int()
    author_id = ma.Int()
    locale = ma.Str()
    start_date = ma.Date()
    end_date = ma.Date()


notification_schema = NotificationSchema()
notifications_schema = NotificationSchema(many=True)
