from __future__ import absolute_import

import os

from celery import Celery, Task
from dotenv import load_dotenv

from casual import celery, create_app

# To run the worker use the following command
#    `celery -A casual.celery_worker:celery worker -l INFO`


# Load the default config files, just like `flask run` does
load_dotenv(".flaskenv")
load_dotenv(".env")


app = create_app()
app.app_context().push()


def make_celery(app):
    celery = Celery(
        app.import_name,
        backend=app.config["RESULT_BACKEND"],
        broker=app.config["BROKER_URL"],
        include=[casual_app for casual_app in app.casual_apps],
    )
    celery.conf.update(app.config)

    class ContextTask(Task):
        abstract = True

        def __call__(self, *args, **kwargs):
            with app.test_request_context():
                res = self.run(*args, **kwargs)
                return res

    celery.Task = ContextTask
    celery.config_from_object(__name__)
    celery.conf.timezone = "UTC"
    return celery


celery = make_celery(app)
