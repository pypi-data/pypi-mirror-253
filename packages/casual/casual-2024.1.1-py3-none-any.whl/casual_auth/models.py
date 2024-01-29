import sqlalchemy as sa
import sqlalchemy.orm as so
from casual import db
from casual.database import CRUDMixin
from casual.util.lists import diff
from flask import abort, request
from flask.globals import current_app
from flask_babel import lazy_gettext as _
from flask_login.mixins import AnonymousUserMixin, UserMixin
from flask_login.utils import current_user
from typing import List
from sqlalchemy.ext.associationproxy import association_proxy
from werkzeug.security import check_password_hash, generate_password_hash

from . import login_manager
from .signals import (
    role_permissions,
    role_users,
    user_changed,
    user_created,
    user_deleted,
    user_email_changed,
    user_roles,
)

user_role = sa.Table(
    "auth_users_roles",
    db.Model.metadata,
    sa.Column("user_id", sa.ForeignKey("auth_users.id", ondelete="CASCADE")),
    sa.Column("role_id", sa.ForeignKey("auth_roles.id", ondelete="CASCADE")),
)

role_permission = sa.Table(
    "auth_roles_permissions",
    db.Model.metadata,
    sa.Column("role_id", sa.ForeignKey("auth_roles.id", ondelete="CASCADE")),
    sa.Column(
        "permission_id",
        sa.ForeignKey("auth_permissions.id", ondelete="CASCADE"),
    ),
)


class User(CRUDMixin, UserMixin, db.Model):
    __tablename__ = "auth_users"

    email: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False, unique=True, index=True)
    username: so.Mapped[str] = so.mapped_column(sa.String(32), nullable=False, unique=True)
    name: so.Mapped[str] = so.mapped_column(sa.String(64))
    locale: so.Mapped[str] = so.mapped_column(sa.String(5), default="en")

    active: so.Mapped[bool] = so.mapped_column(nullable=False, default=True)
    confirmed: so.Mapped[bool] = so.mapped_column(default=False)
    force_pwd_change: so.Mapped[bool] = so.mapped_column(nullable=False, default=False)
    failed_logins: so.Mapped[int] = so.mapped_column(nullable=False, default=0)

    password_hash: so.Mapped[str] = so.mapped_column(sa.String(256), nullable=False)

    _roles: so.Mapped[List["Role"]] = so.relationship(
        "Role", secondary=user_role, backref=so.backref("users", lazy="dynamic")
    )
    roles: so.Mapped[List[str]] = association_proxy("_roles", "name")

    type: so.Mapped[str] = so.mapped_column(sa.String(20))
    __mapper_args__ = {"polymorphic_on": type, "polymorphic_identity": "user"}

    def __str__(self):
        return f"{self.username}"

    def __repr__(self):
        return f"<{self.type}: {self.username}>"

    @property
    def password(self):
        raise AttributeError("´password´ is a readonly attribute")

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password: str) -> bool:
        return check_password_hash(self.password_hash, password)

    def track_failed_logins(self, successful: bool = False) -> None:
        limit = current_app.config["CASUAL_AUTH_LOGIN_FAIL_LIMIT"]
        track = bool(limit)
        original_count = self.failed_logins

        if track:
            if not successful:
                self.failed_logins += 1
            else:
                self.failed_logins = 0

            if self.failed_logins >= limit:
                self.active = False

            if original_count != self.failed_logins:
                self.update()

    @property
    def is_admin(self):
        return self.email in current_app.config["CASUAL_ADMINS"]

    def update_roles(self, selected_roles: list = []) -> None:
        delta = {
            "add": diff(selected_roles, self.roles, False),
            "rem": diff(self.roles, selected_roles, False),
        }

        for role in db.session.scalars(Role.select()):
            if role.name in selected_roles and role not in self._roles:
                self._roles.append(role)
            if role.name not in selected_roles and role in self._roles:
                self._roles.remove(role)

        user_roles.send(self, delta=delta)

    @property
    def permissions(self) -> list:
        """Returns a list of __unique__ permissions"""
        result = list()
        for role in self._roles:
            for permission in role.permissions:
                result.append(permission.name)

        return list(set(result))

    def has_permission(self, permission=None):
        if not permission:
            permission = request.endpoint

        return self.is_admin or permission in self.permissions

    @so.validates("active")
    def validate_active(self, key, value):
        """Validate active status

        Check if the current user tries to deactivate his/her own accout
        and abort if so. Othervise retur the value unmodified."""

        if current_user == self and value is False:
            abort(403, _("You cannot deactivate our own account."))
        return value

    def save(self, commit=True):
        user_created.send(self, current_user=current_user)

        return super().save(commit=commit)

    def update(self, commit=True, **kwargs):
        user_changed.send(self, current_user=current_user)

        return super().update(commit=commit, **kwargs)

    def delete(self, commit=True):
        user_deleted.send(self, current_user=current_user)

        return super().delete(commit=commit)

    @staticmethod
    def on_changed_email(target, value, old_value, initiator):
        """
        When the email changes:

        - update username, based on email (if enabled in config)
        - mark account as NOT confirmed
        - trigger `user_email_changed` signal
        """
        if current_app.config["CASUAL_AUTH_USERNAME_FROM_EMAIL"]:
            target.username = value.split("@")[0]

        if value != old_value:
            target.confirmed = False

            # This is not working as expected because the type of
            # `old_value` is never None.
            if old_value is not None:
                user_email_changed.send(target, new_email=value)

    # Define short aliases for the functions with long names
    hp = has_permission


class Role(CRUDMixin, db.Model):
    __tablename__ = "auth_roles"
    name: so.Mapped[str] = so.mapped_column(sa.String(128))
    description: so.Mapped[str] = so.mapped_column(sa.String(128))
    group: so.Mapped[str] = so.mapped_column(sa.String(128))
    permissions: so.Mapped[List["Permission"]] = so.relationship(
        "Permission",
        secondary=role_permission,
        backref="roles",
    )
    _users = association_proxy("users", "username")
    _permissions = association_proxy("permissions", "name")

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Role: {self.name}>"

    @so.validates("name")
    def validate_name(self, key, value):
        return value.lower()

    @so.validates("group")
    def validate_group(self, key, value):
        return value.capitalize()

    def update_users(self, selected_users=[]):
        delta = {
            "add": diff(selected_users, self._users, False),
            "rem": diff(self._users, selected_users, False),
        }

        users = db.session.scalars(User.select())

        for user in users:
            if user.username in selected_users and user not in self.users:
                self.users.append(user)
            if user.username not in selected_users and user in self.users:
                self.users.remove(user)

        if delta["add"] or delta["rem"]:
            role_users.send(self, delta=delta)

    def update_permissions(self, selected_permissions=[]):
        delta = {
            "add": diff(selected_permissions, self._permissions, False),
            "rem": diff(self._permissions, selected_permissions, False),
        }

        query = Permission.select()
        permissions = db.session.scalars(query)

        for permission in permissions:
            if permission.name in selected_permissions and permission not in self.permissions:
                self.permissions.append(permission)
            if permission.name not in selected_permissions and permission in self.permissions:
                self.permissions.remove(permission)

        if delta["add"] or delta["rem"]:
            role_permissions.send(self, delta=delta)

    @staticmethod
    def on_changed_name(target, value, oldvalue, initiator):
        target.group = value.split("-")[0]


class Permission(CRUDMixin, db.Model):
    __tablename__ = "auth_permissions"
    name: so.Mapped[str] = so.mapped_column(sa.String(128), unique=True)
    group: so.Mapped[str] = so.mapped_column(sa.String(128))
    parent: so.Mapped[str] = so.mapped_column(sa.String(128), default=None)

    def __str__(self) -> str:
        return f"{self.name}"

    def __repr__(self) -> str:
        return f"<Permission: {self.name}>"

    # @so.validates("name")
    # def validate_name(self, key, value):
    #     return value

    @staticmethod
    def on_changed_name(target, value, oldvalue, initiator):
        target.group = value.split(".")[0]


class UserPreference(CRUDMixin, db.Model):
    __tablename__ = "auth_user_preferences"
    name: so.Mapped[str] = so.mapped_column(sa.String(64), nullable=False)
    value: so.Mapped[str] = so.mapped_column(sa.String(64))
    user_id: so.Mapped[str] = so.mapped_column(sa.Integer, sa.ForeignKey("auth_users.id"))
    user: so.Mapped["User"] = so.relationship(
        "User",
        foreign_keys=[user_id],
        backref=so.backref("preferences", lazy="dynamic"),
    )

    def __str__(self):
        return f"<{self.name}>"

    def __repr__(self):
        return f"<Preference: {self.name}>"

    @so.validates("name")
    def validate_name(self, key, value):
        name = value.replace("-", "_")
        name = name.replace(" ", "_")
        return name.upper()

    @so.validates("value")
    def validate_value(self, key, valoare):
        if not valoare:
            return None
        return valoare


class AnonymousUser(AnonymousUserMixin):
    def __str__(self):
        return "<AnonymousUser>"


# User Event Listeners
sa.event.listen(User.email, "set", User.on_changed_email)

# Role Event Listeners
sa.event.listen(Role.name, "set", Role.on_changed_name)

# Permission Event Listeners
sa.event.listen(Permission.name, "set", Permission.on_changed_name)


login_manager.anonymous_user = AnonymousUser


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
