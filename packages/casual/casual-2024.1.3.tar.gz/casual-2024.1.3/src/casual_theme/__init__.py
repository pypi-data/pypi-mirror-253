from flask import Blueprint
from flask_bs4 import Bootstrap

try:
    from importlib.metadata import metadata

    __version__ = metadata("casual")["Version"]
except ImportError:
    __version__ = "2024.0.0"


bootstrap = Bootstrap()


class Theme:
    """Casual Theme. A basic GUI to build upon."""

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        app.config.setdefault("CASUAL_UI_THEME", "theme")
        app.config.setdefault("CASUAL_MAIN_VIEW", "index")

        app.config.setdefault("CASUAL_THEME_DEFAULT_COLOR", "dark")
        app.config.setdefault(
            "CASUAL_THEME_DEFAULT_TABLE",
            " ".join(
                [
                    "table",
                    # 'table-hover',
                    # 'table-bordered',
                    # 'border-primary',
                    # 'table-striped',
                    # 'table-sm',
                    # 'table-dark',
                ]
            ),
        )

        app.config.setdefault("CASUAL_LOCAL_SUBDOMAIN", None)

        blueprint = Blueprint(
            "theme",
            __name__,
            template_folder="templates",
            static_folder="static",
            static_url_path=app.static_url_path + "/theme",
            subdomain=app.config["CASUAL_LOCAL_SUBDOMAIN"],
        )

        bootstrap.init_app(app)

        # Register `casual_theme` to `app.extensions`
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["casual_theme"] = self

        # Register `casual_theme` to `app.casual_apps`
        if not hasattr(app, "casual_apps"):
            app.casual_apps = {}
        app.casual_apps["casual_theme"] = {
            "obj": self,
            "descr": self.__doc__,
            "installable": False,
            "version": __version__,
        }

        def date_conversion(text):
            return f'<span class="date-conversion">{text}<span>'

        app.jinja_env.filters["date"] = date_conversion

        app.register_blueprint(blueprint)

        app.logger.info("Casual Theme started...")
