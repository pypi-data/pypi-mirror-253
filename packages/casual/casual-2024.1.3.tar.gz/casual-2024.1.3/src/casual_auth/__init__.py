from flask.helpers import flash
from flask_babel import lazy_gettext as _
from flask_login import LoginManager, current_user
from flask_login.utils import logout_user

try:
    from importlib.metadata import metadata

    __version__ = metadata("casual")["Version"]
except ImportError:
    __version__ = "2024.0.0"


login_manager = LoginManager()

login_manager.login_view = "auth.login"
login_manager.login_message_category = "info"


class Auth:
    """Core application of Casual to manage users, authentication,
    and authorization."""

    def __init__(self, app=None) -> None:
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("CASUAL_AUTH_REGISTRATION", True)

        app.config.setdefault("CASUAL_AUTH_USERS_PER_PAGE", 10)
        app.config.setdefault("CASUAL_AUTH_ROLES_PER_PAGE", 10)

        login_manager.init_app(app)

        from . import admin  # noqa
        from . import api  # noqa
        from . import hooks  # noqa
        from . import routes  # noqa

        @app.before_request
        def before_request():
            """Logout all users who have been deactivated after
            their login. This applies to all requests to the app,
            not for the blueprint."""

            if current_user.is_authenticated and not current_user.active:
                flash(_("Your account is not active!"), "danger")
                logout_user()

        # Register `Casual_Auth` to `app.extensions`
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["casual_auth"] = self

        # Register `Casual_Auth` to `app.casual_apps`
        if not hasattr(app, "casual_apps"):
            app.casual_apps = {}
        app.casual_apps["casual_auth"] = {
            "obj": self,
            "descr": self.__doc__,
            "installable": True,
            "version": __version__,
        }

        from .blueprints import admin, api_v1, routes  # noqa

        app.register_blueprint(routes)
        app.register_blueprint(admin)
        app.register_blueprint(api_v1)

        app.logger.info("Casual Auth started...")
