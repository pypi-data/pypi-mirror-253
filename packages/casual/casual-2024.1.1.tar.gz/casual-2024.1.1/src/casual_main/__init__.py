from flask_login import login_required

try:
    from importlib.metadata import metadata

    __version__ = metadata("casual")["Version"]
except ImportError:
    __version__ = "2024.0.0"


class Main:
    """Casual Main. Landing page and system notification."""

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("CASUAL_MAIN_VIEW", "main.index")

        from . import admin, routes  # noqa
        from .blueprint import admin_blueprint, route_blueprint  # noqa

        @route_blueprint.before_request
        @login_required
        def before_main_request():
            # pylint: disable=unused-argument
            ...

        # Register `Casual_Main` to `app.extensions`
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["casual_main"] = self

        # Register `Casual_Main` to `app.casual_apps`
        if not hasattr(app, "casual_apps"):
            app.casual_apps = {}
        app.casual_apps["casual_main"] = {
            "obj": self,
            "descr": self.__doc__,
            "installable": True,
            "version": __version__,
        }

        app.register_blueprint(route_blueprint)
        app.register_blueprint(admin_blueprint)

        app.logger.info("Casual Main started...")
