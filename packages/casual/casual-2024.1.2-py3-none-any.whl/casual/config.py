class Config:
    ALCHEMICAL_DATABASE_URL = "sqlite:////"
    ALCHEMICAL_ENGINE_OPTIONS = {
        "echo": False,
        # "echo": True,
    }

    CASUAL_APPS = [
        # ('casual_auth', 'Auth')
    ]
    CASUAL_ADMINS = [
        "username@server.com",
    ]
    CASUAL_DEFAULT_LOCALE = "en"
    CASUAL_LANGUAGES = [
        ("de", "Deutsch"),
        ("en", "English"),
        ("ro", "Română"),
    ]
    CASUAL_NAME = "Casual"

    CASUAL_AUTH_USERNAME_FROM_EMAIL = True
    CASUAL_AUTH_LOGIN_REMEMBER = True
    CASUAL_AUTH_LOGIN_FAIL_LIMIT = 5

    # CASUAL_UI_APP_LOGO = '/static/hagalaz.png'
    # CASUAL_UI_LOGO_CENTER = False

    # Mail configuration
    # https://pythonhosted.org/Flask-Mail/#configuring-flask-mail
    MAIL_SERVER = "mail.server.com"
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_DEBUG = False
    MAIL_USERNAME = "username@server.com"
    MAIL_PASSWORD = "Pa$$w0rd"
    # MAIL_MAX_EMAILS = None
    # MAIL_SUPPRESS_SEND = True
    # MAIL_ASCII_ATTACHMENTS = False
    MAIL_DEFAULT_SENDER = (CASUAL_NAME, CASUAL_ADMINS[0])
