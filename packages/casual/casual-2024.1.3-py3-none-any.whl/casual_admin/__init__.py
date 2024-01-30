"""
    casual_admin
    ~~~~~~~~~~

    Implements an admin blueprint to connect other blueprint's admin pages together.

    :copyright: (c) 2023 by Horia Filimonescu.
    :license: MIT, see LICENSE for more details.
"""

try:
    from importlib.metadata import metadata

    __version__ = metadata("casual")["Version"]
except ImportError:
    __version__ = "2024.0.0"


class Admin:
    """Casual Admin Package"""

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app=None):
        # Set default config parameters
        app.config.setdefault("CASUAL_ADMIN_CARDS_ROW", 4)
        app.config.setdefault("CASUAL_ADMIN_CARDS_DESIGN", "light")

        from . import routes  # noqa

        # Register `Casual_Admin` to `app.extensions`
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["casual_admin"] = self

        # Register `Casual_Admin` to `app.casual_apps`
        if not hasattr(app, "casual_apps"):
            app.casual_apps = {}
        app.casual_apps["casual_admin"] = {
            "obj": self,
            "descr": self.__doc__,
            "installable": True,
            "version": __version__,
        }

        # Register blueprint
        # fmt: off
        from .bp import bp
        app.register_blueprint(bp)
        # fmt: on

        app.logger.info("Casual Admin started...")
