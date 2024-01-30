from flask import redirect, render_template
from flask.helpers import flash, url_for
from flask_babel import lazy_gettext as _
from flask_login import current_user, login_required

from ..blueprints import routes as bp
from ..emails import user_confirmation_email


@bp.route("/confirm/<token>/")
@login_required
def confirm(token):
    if current_user.confirmed:
        flash("Your account is already confirmed.", "info")
        return redirect(url_for("main.index"))

    if current_user.confirm(token):
        flash("You have confirmed your account. Thanks!", "success")
    else:
        flash("The confirmation link is invalid or has expired.", "warning")
        return redirect(url_for("auth.unconfirmed"))

    return render_template("auth/routes.base.html.j2")


@bp.route("/confirm/")
@login_required
def unconfirmed():
    if current_user.confirmed:
        flash(_("Your email is already confirmed"), "warning")
        return redirect(url_for("main.index"))

    return render_template("auth/routes.confirm.html.j2")


@bp.route("/confirmation/mail/")
@login_required
def send_confirmation():
    if current_user.confirmed:
        flash(_("Your email is already confirmed"), "warning")
        return redirect(url_for("main.index"))

    user_confirmation_email(current_user)
    flash(_("A confirmation email has been sent to you by email."), "success")
    return redirect(url_for("main.index"))
