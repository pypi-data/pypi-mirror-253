import gettext

from flask import render_template

from casual.util.email import send_async_email

_ = gettext.gettext


def user_new_email(user, password):
    send_async_email.delay(
        subject=_("Your New Account"),
        recipients=[user.email],
        text_body=render_template("auth/email.user_new.txt.j2", password=password, user=user),
        html_body=render_template("auth/email.user_new.html.j2", password=password, user=user),
    )


def user_change_email(user, new_email):
    send_async_email.delay(
        subject=_("Email for %(name)s has changed.", name=user.name),
        recipients=[user.email, new_email],
        text_body=render_template(
            "auth/email.user_change_email.txt.j2",
            user=user,
            old_email=user.email,
            new_email=new_email,
        ),
        html_body=render_template(
            "auth/email.user_change_email.html.j2",
            user=user,
            old_email=user.email,
            new_email=new_email,
        ),
    )


def user_reset_password(user, password):
    send_async_email.delay(
        subject=_("Password Reset"),
        recipients=[user.email],
        text_body=render_template(
            "auth/email.user_reset_password.txt.j2",
            user=user,
            password=password,
        ),
        html_body=render_template(
            "auth/email.user_reset_password.html.j2",
            user=user,
            password=password,
        ),
    )


def user_confirmation_email(user) -> None:
    if not hasattr(user, "email"):
        return
    send_async_email.delay(
        subject=_("Email Confirmation"),
        recipients=[user.email],
        text_body=render_template("auth/email.user_confirm_email.txt.j2", user=user),
        html_body=render_template("auth/email.user_confirm_email.html.j2", user=user),
    )
