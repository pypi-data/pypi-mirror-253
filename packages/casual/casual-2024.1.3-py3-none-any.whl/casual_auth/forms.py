import gettext

from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    EmailField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
)
from wtforms.validators import (
    DataRequired,
    Email,
    EqualTo,
    Length,
    Optional,
    Regexp,
    ValidationError,
)

from casual import db
from casual_auth.models import Role, User

_ = gettext.gettext


class LoginForm(FlaskForm):
    username_or_email = StringField(
        _("Username or Email"),
        render_kw={"autofocus": "autofocus"},
        validators=[DataRequired(), Length(5, 64)],
    )

    password = PasswordField(_("Password"), validators=[DataRequired()])

    remember_me = BooleanField(_("Remember me"), default=False)

    submit = SubmitField(_("Login"))


class RegistrationForm(FlaskForm):
    email = StringField(
        _("Email"),
        render_kw={"autofocus": "autofocus"},
        validators=[DataRequired(), Length(1, 64)],
    )

    password = PasswordField(
        _("Password"),
        validators=[
            DataRequired(),
            EqualTo("confirm_password", message=_("Passwords must match")),
        ],
    )

    confirm_password = PasswordField(_("Confirm Password"), validators=[DataRequired()])

    submit = SubmitField(_("Register"))

    def validate_email(self, email):
        query = User.select().filter_by(email=email.data)
        user = db.session.scalar(query)
        if user is not None:
            raise ValidationError(_("Please use a different email."))


class ChangePasswordForm(FlaskForm):
    old_password = PasswordField(
        _("Old password"),
        render_kw={"autofocus": "autofocus"},
        validators=[DataRequired()],
    )
    password = PasswordField(
        _("New password"),
        validators=[
            DataRequired(),
            Length(5, 32),
            # Regexp('[A-Za-z0-9@#$%^&+=]'),
            EqualTo("password2", message=_("Passwords must match")),
        ],
    )
    password2 = PasswordField(_("Confirm new password"), validators=[DataRequired(), Length(5, 32)])
    submit = SubmitField(_("Update Password"))


class ResetPasswordForm(FlaskForm):
    email = StringField(
        _("Email"),
        render_kw={"autofocus": "autofocus"},
        validators=[
            Email(),
            DataRequired(),
            Length(1, 64),
        ],
    )
    submit = SubmitField(_("Reset Password"))


class PreferenceForm(FlaskForm):
    name = StringField(
        _("Key"),
        render_kw={"autofocus": "autofocus"},
        validators=[
            DataRequired(),
            Length(1, 64),
        ],
    )
    value = StringField(
        _("Value"),
        validators=[
            Optional(),
            Length(0, 64),
        ],
    )
    submit = SubmitField(_("Save"))


class AdminUserForm(FlaskForm):
    username = StringField(
        _("Username"),
        render_kw={"autofocus": "autofocus"},
        validators=[
            DataRequired(),
            Length(5, 64),
        ],
    )
    name = StringField(
        _("Full Name"),
        render_kw={"autofocus": "autofocus"},
        validators=[
            DataRequired(),
            Length(1, 64),
        ],
    )
    email = EmailField(
        _("Email"),
        validators=[
            DataRequired(),
            Length(6, 64),
            Email(),
        ],
    )
    locale = SelectField(_("Language"))
    active = BooleanField(_("Active User"), default=True)


class AdminUserCreateForm(AdminUserForm):
    submit = SubmitField(_("Create User"))

    def validate_email(self, email):
        query = User.select().filter_by(email=email.data)
        if db.session.scalar(query) is not None:
            raise ValidationError(_("Email %(mail)s is already registered.", mail=(email.data)))


class AdminUserEditForm(AdminUserForm):
    submit = SubmitField(_("Update User"))


class AdminUserRoleForm(FlaskForm):
    submit = SubmitField(_("Assign Roles"))


class AdminRoleForm(FlaskForm):
    name = StringField(
        _("Name"),
        render_kw={"autofocus": "autofocus"},
        validators=[
            DataRequired(),
            Length(5, 32),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_-]*$",
                0,
                _(
                    "Role names are allowed only letters, numbers, "
                    "or underscores. They must start with a letter."
                ),
            ),
        ],
        description=_("The preffered format is `group-other_info`."),
    )
    description = StringField(
        _("Description"),
        render_kw={"autocomplete": "off"},
        validators=[
            DataRequired(),
            Length(1, 128),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_ -]*$",
                0,
                _(
                    "Role descriptions are allowed only letters, numbers, "
                    "or underscores. They must start with a letter."
                ),
            ),
        ],
    )
    submit = SubmitField(_("Save"))


class AdminRoleCreateForm(AdminRoleForm):
    def validate_name(self, name):
        query = Role.select().filter_by(name=name.data)
        role = db.session.scalar(query)

        if role is not None:
            raise ValidationError(_("Please use a different name."))
