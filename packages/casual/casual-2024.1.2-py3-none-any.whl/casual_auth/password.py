import secrets


def password_generator(length: int = 12) -> str:
    return secrets.token_urlsafe(length)
