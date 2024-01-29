from flask import abort, redirect, render_template, request, session
from flask.globals import current_app
from flask.helpers import flash, url_for
from flask_babel import lazy_gettext as _
from flask_babel import ngettext
from flask_login import current_user, login_required, login_user, logout_user
from flask_menu import register_menu
from sqlalchemy import and_

from casual import db
from casual_auth.decorators import check_permission
from casual_auth.emails import user_reset_password
from casual_auth.forms import (
    ChangePasswordForm,
    LoginForm,
    PreferenceForm,
    ResetPasswordForm,
)
from casual_auth.models import User, UserPreference
from casual_auth.password import password_generator

from ..blueprints import routes as bp
from . import confirmation, registration


@bp.before_app_request
def before_app_request():
    if current_user.is_authenticated:
        if (
            current_user.force_pwd_change
            and request.endpoint[:5] != "auth."
            and request.endpoint[:7] != "static."
            and request.endpoint[:13] != "debugtoolbar."
        ):
            return redirect(url_for("auth.change_password"))
        if (
            not current_user.confirmed
            and request.endpoint[:5] != "auth."
            and request.endpoint[:7] != "static."
            and request.endpoint[:13] != "debugtoolbar."
        ):
            return redirect(url_for("auth.unconfirmed"))


@bp.route("/", methods=["GET", "POST"])
@register_menu(bp, ".auth", _("Login"), visible_when=lambda: False)
def login():
    if current_user.is_authenticated:
        flash(
            _(
                "You were already authenticated as %(name)s.",
                name=(current_user.name),
            ),
            "info",
        )
        logout_user()

    form = LoginForm()

    if form.validate_on_submit():
        _fails = 0

        user = User.read(form.username_or_email.data)

        if user is None:
            flash(_("Invalid username or password."), "danger")
            return redirect(url_for("auth.login"))

        _fails = user.failed_logins

        verification = user.verify_password(form.password.data)

        user.track_failed_logins(verification)

        if not verification:
            flash(_("Invalid username or password."), "danger")
            return redirect(url_for("auth.login"))

        if _fails > 0:
            flash(
                ngettext(
                    "You have %(num)d failed login attempt.",
                    "You have %(num)d failed login attempts.",
                    num=_fails,
                ),
                "warning",
            )

        if not current_app.config["CASUAL_AUTH_LOGIN_REMEMBER"]:
            form.remember_me.data = False

        login_user(user, remember=form.remember_me.data)

        return redirect(request.args.get("next") or url_for("main.index"))

    return render_template("auth/routes.login.html.j2", form=form)


@bp.route("/logout/")
@register_menu(
    bp,
    ".auth.logout",
    _("Logout"),
    order=90,
    visible_when=lambda: current_user.is_authenticated,
    icon="lock",
    divided=True,
)
@login_required
def logout():
    logout_user()

    session.pop("preferences", None)
    session.pop("locale", None)

    flash(_("You have been logged out."), "info")
    return redirect(url_for("auth.login"))


@bp.route("/reset_password/", methods=["GET", "POST"])
def reset_password():
    form = ResetPasswordForm()

    if form.validate_on_submit():
        query = User.select().filter_by(email=form.email.data)
        user = db.session.scalar(query)

        if user is None:
            flash(_("Please provide a valid email."), "danger")
            return redirect(url_for("auth.reset_password"))
        if not user.active:
            flash(
                _("Your account is not active. Please contact the administrator."),
                "error",
            )
            return redirect(url_for("auth.login"))
        if user.force_pwd_change:
            flash(_("You have already resetted your password!"), "info")
            return redirect(url_for("auth.login"))

        password = password_generator(16)

        if current_app.config["DEBUG"]:
            print(password)

        user.force_pwd_change = True
        user.password = password

        form.populate_obj(user)
        if user.update():
            flash(
                _("Your password has been reset. Check your Email account."),
                "success",
            )
            user_reset_password(user, password)

        return redirect(url_for("auth.login"))
    return render_template("auth/routes.reset_password.html.j2", form=form)


@bp.route("/change_password/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".auth.change_password",
    _("Change Password"),
    order=30,
    visible_when=lambda: current_user.is_authenticated,
    icon="key",
)
@login_required
def change_password():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        if current_user.verify_password(form.old_password.data):
            current_user.password = form.password.data
            current_user.force_pwd_change = False
            if current_user.update():
                flash(_("Your password has been updated."), "success")
                return redirect(url_for("auth.login"))
        else:
            flash(_("Invalid password."), "danger")
    return render_template("auth/routes.change_password.html.j2", form=form)


@bp.route("/profile/")
@register_menu(
    bp,
    ".auth.profile",
    _("My Profile"),
    order=10,
    visible_when=lambda: current_user.is_authenticated,
    icon="person-square",
)
def profile():
    return render_template(
        "auth/routes.user.profile.html.j2",
        user=current_user,
    )


@bp.route("/preference/")
@register_menu(
    bp,
    "auth.preference",
    _("Preferences"),
    order=20,
    visible_when=lambda: current_user.is_authenticated,
    icon="sliders",
)
@check_permission
def preferences():
    form = PreferenceForm()

    return render_template(
        "auth/routes.preference.list.html.j2",
        form=form,
        preferences=current_user.preferences,
        user=current_user,
    )


@bp.route("/preference/create/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".auth.preference.create",
    _("Add Preference"),
    icon="plus-square",
    order=10,
    type="primary",
    visible_when=lambda: False,
    pagemenu=lambda: True,
)
@check_permission
def preference_create():
    form = PreferenceForm()

    if form.validate_on_submit():
        tmp = UserPreference(name=form.name.data)

        query = UserPreference.select().filter(
            and_(
                UserPreference.name == tmp.name,
                UserPreference.user_id == current_user.id,
            )
        )
        preference = db.session.scalar(query)

        if not preference:
            preference = UserPreference()

        form.populate_obj(preference)
        preference.user_id = current_user.id

        preference.update()

        session.pop("preferences", None)
        session["preferences"] = {}

        for pref in current_user.preferences:
            session["preferences"][pref.name] = pref.value

        flash(_("Preference has been saved"), "success")

        return redirect(url_for("auth.preferences"))

    for field, errors in form.errors.items():
        for error in errors:
            flash(
                _(
                    "%(field)s: %(msg)s",
                    field=(getattr(form, field).label.text),
                    msg=error,
                ),
                "danger",
            )

    return render_template("auth/routes.preference.edit.html.j2", form=form, user=current_user)


@bp.route("/preference/<int:id>/delete/", methods=["GET", "POST"])
@register_menu(
    bp,
    ".auth.preference.delete",
    _("Delete"),
    icon="trash",
    order=10,
    type="danger",
    visible_when=lambda: False,
    endpoint_arguments_constructor=lambda: dict(id=0),
    itemmenu=lambda: current_user.is_authenticated,
)
@check_permission
def preference_delete(id):
    preference = UserPreference.read(id) or abort(404)
    preference.delete()
    flash(_("Your preference key has been deleted."), "warning")
    return redirect(url_for("auth.preferences"))


@bp.route("/preference/reload/")
@register_menu(
    bp,
    ".auth.preference.reload",
    _("Reload Preferences"),
    order=20,
    icon="arrow-repeat",
    type="info",
    visible_when=lambda: False,
    pagemenu=lambda: True,
)
@check_permission
def preference_reload():
    session.pop("preferences", None)
    session["preferences"] = {}

    for preference in current_user.preferences:
        session["preferences"][preference.name] = preference.value

    flash(
        _(
            "Preferences for %(name)s have been reloaded.",
            name=(current_user.name or current_user.username),
        ),
        "success",
    )

    return redirect(url_for("auth.preferences"))
