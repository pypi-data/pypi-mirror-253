from flask import redirect
from flask.helpers import flash, url_for
from flask.templating import render_template
from flask_babel import lazy_gettext as _

from casual_auth.forms import RegistrationForm
from casual_auth.models import User

from ..blueprints import routes as bp


@bp.route("/register/", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User()
        form.populate_obj(user)
        user.save()

        flash(_("You have registered sucessfuly"), "success")

        return redirect(url_for("auth.login"))

    return render_template(
        "auth/routes.register.html.j2",
        form=form,
    )
