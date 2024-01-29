from flask import json, render_template, request
from werkzeug.exceptions import HTTPException

try:
    from importlib.metadata import metadata

    __version__ = metadata("casual")["Version"]
except ImportError:
    __version__ = "2024.0.0"


class Error:
    """Error Handler for the Casual Framework"""

    def __init__(self, app=None):
        if app:
            self.init_app(app)

    def init_app(self, app):
        # Register `Casual_Error` to `app.extensions`
        if not hasattr(app, "extensions"):
            app.extensions = {}
        app.extensions["casual_error"] = self

        # Register `Casual_Error` to `app.casual_apps`
        if not hasattr(app, "casual_apps"):
            app.casual_apps = {}
        app.casual_apps["casual_error"] = {
            "obj": self,
            "descr": self.__doc__,
            "installable": False,
            "version": __version__,
        }

        from .blueprints import blueprint  # noqa

        @app.errorhandler(HTTPException)
        def handle_exception(e):
            """Generic Exception Handlers

            source: https://flask.palletsprojects.com/en/1.1.x/errorhandling/#generic-exception-handlers
            """
            # pylint: disable=unused-variable

            if request.is_json:
                """Return JSON instead of HTML for HTTP errors."""
                response = e.get_response()

                # replace the body with JSON
                response.data = json.dumps(
                    {
                        "code": e.code,
                        "name": e.name,
                        "description": e.description,
                        "version": __version__,
                    }
                )
                response.content_type = "application/json"
                return response

            return render_template("errors/generic_error.html.j2", error=e), 404

        app.register_blueprint(blueprint)

        app.logger.info("Casual Error started...")
