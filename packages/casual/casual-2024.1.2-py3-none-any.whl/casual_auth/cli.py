import click
from flask import current_app
from flask.cli import with_appcontext


@click.group()
def auth():
    """Casual A12n and A11n commands"""
    pass


@auth.command()
@with_appcontext
def create_admins():
    """Create the dedicated user"""
    from casual import db  # noqa
    from casual_auth.models import User  # noqa

    admin_list = current_app.config.get("CASUAL_ADMINS")

    for admin in admin_list:
        username = admin.split("@")[0]
        query = User.select().filter_by(email=admin)
        user = db.session.scalar(query)

        if user is not None:
            click.secho(f"User {admin} already exists...", fg="yellow")
        else:
            click.secho(f"Creating user {admin}...", fg="cyan")
            auser = User()
            auser.email = admin
            auser.username = username
            auser.password = "Casual"
            auser.name = username
            auser.locale = "en"
            auser.force_pwd_change = True
            auser.confirmed = True
            db.session.add(auser)
            click.secho(f"Created user {admin}.", fg="green")

    db.session.commit()
