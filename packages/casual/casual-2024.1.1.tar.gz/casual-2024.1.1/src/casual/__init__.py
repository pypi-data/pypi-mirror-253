import importlib
import logging
import os
from collections import defaultdict
from logging.handlers import RotatingFileHandler, SMTPHandler

from alchemical.flask import Alchemical
from celery import Celery
from casual_admin import Admin
from casual_auth import Auth
from casual_basis import Basis
from casual_error import Error
from casual_main import Main
from casual_theme import Theme
from flask import Flask
from flask.globals import current_app, request, session
from flask_babel import Babel
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import current_user as cu
from flask_mail import Mail
from flask_marshmallow import Marshmallow
from flask_menu import Menu
from flask_migrate import Migrate

from .config import Config

try:
    from importlib.metadata import metadata

    __version__ = metadata("casual")["Version"]
except ImportError:
    __version__ = "2024.0.0"


# https://stackoverflow.com/a/46785675
# https://github.com/miguelgrinberg/Flask-Migrate/issues/61#issuecomment-208131722
naming_convention = {
    "ix": "ix_%(column_0_label)s",
    "uq": "uq_%(table_name)s_%(column_0_name)s",
    "ck": "ck_%(table_name)s_%(column_0_name)s",
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
    "pk": "pk_%(table_name)s",
}


babel = Babel()
celery = Celery(__name__)
# db = SQLAlchemy(metadata=MetaData(naming_convention=naming_convention))
db = Alchemical()
ma = Marshmallow()
mail = Mail()
menu = Menu()
migrate = Migrate()
toolbar = DebugToolbarExtension()


casual_admin = Admin()
casual_auth = Auth()
casual_basis = Basis()
casual_error = Error()
casual_main = Main()
casual_theme = Theme()


def get_locale():
    if cu.is_authenticated and cu.locale is not None:
        session["locale"] = cu.locale
        return cu.locale
    else:
        # Returns the first tuple element from a list of tuples
        guess = request.accept_languages.best_match(
            [lang[0] for lang in current_app.config["CASUAL_LANGUAGES"]]
        )
        # [lang[0] for lang in Config.CASUAL_LANGUAGES])
        session["locale"] = guess
        return guess
    # if session.get('locale'):
    #     return session['locale']


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)

    # Load default config of the project
    app.config.from_object(Config)

    if test_config is None:
        app.config.from_envvar("CASUAL_CONF", silent=True)
    else:
        app.config.update(test_config)

    # Make sure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Celery initialization
    celery.conf.update(app.config)

    # Check if the db is sqlite. Needed by `render_as_batch` in
    # `migrate.init_app`
    is_sqlite = app.config["ALCHEMICAL_DATABASE_URL"].startswith("sqlite://")

    # Create `app.casual_apps`
    if not hasattr(app, "casual_apps"):
        app.casual_apps = defaultdict()

    # Worth reading about logging
    # https://flask.palletsprojects.com/en/1.1.x/quickstart/#logging
    if app.debug and not app.testing:
        if app.config["MAIL_SERVER"]:
            auth = None
            secure = None

            if app.config["MAIL_USERNAME"] or app.config["MAIL_PASSWORD"]:
                auth = (
                    app.config["MAIL_USERNAME"],
                    app.config["MAIL_PASSWORD"],
                )
            if app.config["MAIL_USE_TLS"]:
                secure = ()

            mail_handler = SMTPHandler(
                mailhost=(app.config["MAIL_SERVER"], app.config["MAIL_PORT"]),
                fromaddr="no-reply@" + app.config["MAIL_SERVER"],
                toaddrs=app.config["CASUAL_ADMINS"],
                subject="{} Failure".format(app.config["CASUAL_NAME"]),
                credentials=auth,
                secure=secure,
            )
            mail_handler.setLevel(logging.ERROR)
            app.logger.addHandler(mail_handler)

        if app.config["CASUAL_LOG_STDOUT"]:
            stream_handler = logging.StreamHandler()
            stream_handler.setLevel(logging.DEBUG)
            app.logger.addHandler(stream_handler)
        else:
            # Define the log details
            log_path = os.path.join(app.instance_path, "log")
            log_file = app.config["CASUAL_NAME"] + ".log"

            # Ensure the log folder exists
            try:
                os.makedirs(log_path)
            except OSError:
                pass

            file_handler = RotatingFileHandler(
                os.path.join(log_path, log_file),
                maxBytes=1048576,
                backupCount=20,
            )
            file_handler.setFormatter(
                logging.Formatter(
                    "%(asctime)s %(levelname)s: %(message)s " "[%(pathname)s: %(lineno)d]"
                )
            )
            file_handler.setLevel(logging.INFO)
            app.logger.addHandler(file_handler)

    # Initialize Flask extensions
    babel.init_app(app, locale_selector=get_locale)
    db.init_app(app)
    ma.init_app(app)
    mail.init_app(app)
    menu.init_app(app)
    migrate.init_app(app, db, render_as_batch=is_sqlite)
    toolbar.init_app(app)

    # Initialize default Casual apps
    casual_auth.init_app(app)
    casual_error.init_app(app)
    casual_basis.init_app(app)
    casual_main.init_app(app)
    casual_theme.init_app(app)

    # Automatically load the applications listed in the config file
    for pkg_name, pkg_class in app.config.get("CASUAL_APPS", []):
        if pkg_name not in app.casual_apps:
            pkg_instance = importlib.import_module(pkg_name)
            pkg_object = getattr(pkg_instance, pkg_class)
            pkg_object(app)

    casual_admin.init_app(app)

    # Import generally available hooks.
    from . import hooks  # noqa

    # app.context_processor(lambda: dict(menu=app.url_map.iter_rules()))

    return app
