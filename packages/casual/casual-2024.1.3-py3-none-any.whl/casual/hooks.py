from flask.globals import current_app

from .signals import log_signal


@log_signal.connect
def log_signal_hook(sender, action, **extra):
    current_app.logger.info(f"{sender} was {action}")
