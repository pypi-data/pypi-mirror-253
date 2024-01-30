from flask.globals import current_app, session
from flask_login.signals import user_logged_in, user_logged_out

from ..emails import user_change_email, user_confirmation_email, user_new_email
from ..signals import (user_changed, user_created, user_deleted,
                       user_email_changed, user_roles)


@user_logged_in.connect
def user_login_hook(sender, user, **extra):
    session['locale'] = user.locale

    if session.get('preferences', None) is None:
        session['preferences'] = {}
    for preference in user.preferences:
        session['preferences'][preference.name] = preference.value


@user_logged_out.connect
def user_logout_hook(sender, user, **extra):
    if 'preferences' in session:
        session.pop('preferences')
    if 'locale' in session:
        session.pop('locale')


@user_roles.connect
def user_roles_hook(sender, delta, **extra):
    current_app.logger.critical(
        f'{sender.username} roles changed {delta}'
    )


@user_deleted.connect
def user_deleted_hook(user, current_user, **extra):
    current_app.logger.warning(
        f'`{current_user.username}` deleted `{user}`')


@user_created.connect
def user_created_hook(sender, current_user, **extra):
    """Hook for new users

    -   IMPORTANT: The email with the new password will be sent 
        from the route
    -   Send the confirmation mail to the new address
    -   Log who created the new user for documentataion purposes
    """

    current_app.logger.info('---- Test ----')

    # user_confirmation_email(sender)
    # user_new_mail(sender)

    if current_user.is_anonymous:
        current_app.logger.info(
            f'`{sender.username}` registered himself.')
    else:
        current_app.logger.info(
            f'`{current_user}` created `{sender.username}`')


@user_email_changed.connect
def user_email_changed_hook(sender, new_email, **extra):
    """Hook for changed email addresses

    - Send the confirmation mail to the new address
    - Send the notification mail to __both__ addresses
    - Log the change for documentataion purposes

    In this case the `sender` is the _unupdated_ user. Thus the old email 
    address is being extracted from the sender and the new email is passed 
    as `new_email`.
    """

    # If the `sender.email` is not present it is not of type None, but
    # of type `<class 'NoneType'>` from SQLAlchemy

    if isinstance(sender.email, str):
        user_confirmation_email(sender)
        user_change_email(sender, new_email)

        current_app.logger.info(
            f'`{sender.username}` changed the email address '
            f'from `{sender.email}` to `{new_email}`')
