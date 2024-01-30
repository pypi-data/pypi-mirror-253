from casual_auth.signals import role_changed, role_created, role_deleted, role_permissions, role_users
from flask.globals import current_app


@role_created.connect
def role_created_hook(sender, role, **extra):
    current_app.logger.info(f"Role `{role}` created")


@role_changed.connect
def role_changed_hook(sender, role, **extra):
    current_app.logger.info(f"Role `{role}` changed")


@role_deleted.connect
def role_deleted_hook(sender, role, **extra):
    current_app.logger.info(f"Role `{role}` deleted")


@role_permissions.connect
def role_permissions_hook(sender, delta, **extras):
    current_app.logger.info(f"Role `{sender.name}` changed permissions {delta}")


@role_users.connect
def role_users_hook(sender, delta, **extra):
    current_app.logger.info(f"{sender.name} users changed {delta}")
