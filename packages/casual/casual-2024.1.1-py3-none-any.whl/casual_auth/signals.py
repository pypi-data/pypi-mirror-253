from blinker import Namespace

auth = Namespace()


role_created = auth.signal('role_created')
role_changed = auth.signal('role_changed')
role_deleted = auth.signal('role_deleted')
role_permissions = auth.signal('role_permissions')
role_users = auth.signal('role_users')


# User created by another user
user_created = auth.signal('user_created')

user_read = auth.signal('user_read')
user_changed = auth.signal('user_changed')
user_deleted = auth.signal('user_deleted')
user_roles = auth.signal('user_roles')

# Active status of a user changes
user_active_status = auth.signal('user_active_status')

# `failed_logins` counter changes
user_login_failed = auth.signal('user_login_failed')


user_email_changed = auth.signal('user_email_changed')
