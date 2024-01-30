from flask import Blueprint

blueprint = Blueprint(
    "error",
    __name__,
    template_folder="templates",
)
