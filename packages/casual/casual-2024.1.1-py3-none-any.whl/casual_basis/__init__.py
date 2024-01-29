try:
    from importlib.metadata import metadata

    __version__ = metadata("casual")["Version"]
except ImportError:
    __version__ = "2024.0.0"


class Basis:
    """Casual Basis. Tools to manage the app and modules"""

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        from . import admin  # noqa
        from . import hooks  # noqa
        from .blueprints import admin_blueprint, routes_blueprint  # noqa

        # Register `Casual_Basis` to `app.extensions`
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["casual_basis"] = self

        # Register `Casual_Basis` to `app.casual_apps`
        if not hasattr(app, "casual_apps"):
            app.casual_apps = {}

        app.casual_apps["casual_basis"] = {
            "obj": self,
            "descr": self.__doc__,
            "installable": True,
            "version": __version__,
        }

        app.register_blueprint(routes_blueprint)
        app.register_blueprint(admin_blueprint)

        app.logger.info("Casual Basis started...")
