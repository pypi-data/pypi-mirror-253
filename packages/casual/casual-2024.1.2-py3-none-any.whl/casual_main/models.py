from datetime import date, timedelta

from bleach import clean, linkify
from flask.globals import session
from markdown import markdown
from pycountry import countries
from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    Text,
    and_,
    event,
)
from sqlalchemy.orm import backref, relationship

from casual import db
from casual.database import CRUDMixin

from . import conf_markdown as mkd


class Notification(CRUDMixin, db.Model):
    __tablename__ = "main_messages"

    locale = Column(String(5), default="en")
    body = Column(Text, nullable=False)
    body_html = Column(Text)
    author_id = Column(Integer, ForeignKey("auth_users.id"))
    author = relationship(
        "User",
        foreign_keys=[author_id],
        backref=backref("messages", lazy="dynamic"),
    )
    start_date = Column(Date, nullable=False, default=date.today())
    end_date = Column(Date, nullable=False, default=date.today() + timedelta(days=7))

    def __repr__(self) -> str:
        return f"<Notification #{self.id}>"

    @property
    def visible(self):
        return self.start_date <= date.today() <= self.end_date

    @property
    def expired(self):
        return self.end_date < date.today()

    @property
    def flag(self):
        return countries.get(alpha_2=self.locale).flag

    @classmethod
    def list(cls) -> list:
        notifications = db.session.scalars(
            cls.select().where(
                and_(
                    cls.start_date <= date.today(),
                    cls.end_date >= date.today(),
                    cls.locale == session.get("locale"),
                )
            )
        ).fetchall()

        return notifications

    @classmethod
    def clean_up(cls) -> int:
        counter = 0

        notifications = db.session.scalars(cls.select())
        for notification in notifications:
            if notification.expired:
                counter += 1
                notification.delete()

        return counter

    @staticmethod
    def on_changed_body(target, value, oldvalue, initiator):
        target.body_html = linkify(
            clean(
                markdown(
                    value,
                    output_format="html",
                    extensions=mkd.allowed_extensions,
                ),
                tags=mkd.allowed_tags,
                attributes=mkd.allowed_attrs,
                strip=True,
            )
        )


event.listen(Notification.body, "set", Notification.on_changed_body)
