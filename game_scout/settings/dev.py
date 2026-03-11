from .base import *  # noqa: F403,F401

DEBUG = env.bool("DJANGO_DEBUG", default=True)  # type: ignore[name-defined]
ALLOWED_HOSTS = env.list("DJANGO_ALLOWED_HOSTS", default=["127.0.0.1", "localhost"])  # type: ignore[name-defined]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
