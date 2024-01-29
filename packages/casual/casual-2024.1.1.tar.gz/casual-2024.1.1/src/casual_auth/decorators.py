from functools import wraps

from flask import flash, request
from flask_babel import lazy_gettext as _
from flask_login.utils import current_user, login_required
from werkzeug.exceptions import abort


def permission_required(arg=None):
    def decorator(f):
        @login_required
        @wraps(f)
        def wrapper(*args, **kwargs):
            perm = arg

            if callable(arg) or arg is None:
                perm = request.endpoint

            if current_user.has_permission(perm):
                return f(*args, **kwargs)

            msg = None

            if request.is_json:
                msg = _("Missing permission %(perm)s", perm=perm)
            else:
                flash(_("Missing permission %(perm)s", perm=perm), "warning")
            abort(403, msg)

        return wrapper

    if callable(arg):
        return decorator(arg)

    return decorator


check_permission = permission_required
