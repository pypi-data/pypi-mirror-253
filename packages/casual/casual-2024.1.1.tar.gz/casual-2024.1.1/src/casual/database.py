from datetime import datetime

from flask import abort
from sqlalchemy import Column, DateTime, ForeignKey, Integer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.ext.declarative import declared_attr
import sqlalchemy.orm as so
from sqlalchemy_continuum.plugins.flask import fetch_current_user_id

from casual import db

from .signals import log_signal


class CRUDMixin:
    __table_args__ = {"extend_existing": True}
    __log_signals__ = True

    id: so.Mapped[int] = so.mapped_column(primary_key=True)

    @classmethod
    def read(cls, id) -> object or None:
        if any(
            (
                isinstance(id, (str, bytes)) and id.isdigit(),
                isinstance(id, (int, float)),
            )
        ):
            return db.session.get(cls, int(id)) or abort(404)

        if isinstance(id, (str, bytes)) and not id.isdigit():
            if "@" in id:
                query = cls.select().where(cls.email == id)

            else:
                query = cls.select().where(cls.username == id)

            return db.session.scalar(query) or abort(404)
        return None

    def _save(self, commit=True):
        db.session.add(self)
        if commit:
            try:
                db.session.commit()
            except IntegrityError:
                abort(409)
        return self

    def update(self, commit=True, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

        if self.__log_signals__:
            log_signal.send(self, action="updated")

        return commit and self._save() or self

    def save(self, commit=True):
        if self.__log_signals__:
            log_signal.send(self, action="created")

        return commit and self._save() or self

    def delete(self, commit=True):
        if self.__log_signals__:
            log_signal.send(self, action="deleted")

        db.session.delete(self)
        return commit and db.session.commit()


class AuditMixin:
    __table_args__ = {"extend_existing": True}

    create_time = Column(DateTime, default=datetime.utcnow)
    change_time = Column(DateTime(), onupdate=datetime.utcnow)

    @declared_attr
    def create_id(cls):
        return Column(
            Integer,
            ForeignKey("auth_users.id"),
            default=fetch_current_user_id,
        )

    @declared_attr
    def create_by(cls):
        return so.relationship(
            "User",
            primaryjoin="%s.create_id == User.id" % cls.__name__,
            enable_typechecks=False,
        )

    @declared_attr
    def change_id(cls):
        return Column(
            Integer,
            ForeignKey("auth_users.id"),
            onupdate=fetch_current_user_id,
        )

    @declared_attr
    def change_by(cls):
        return so.relationship(
            "User",
            primaryjoin="%s.change_id == User.id" % cls.__name__,
            enable_typechecks=False,
        )
