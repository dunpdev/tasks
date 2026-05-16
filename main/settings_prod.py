from .settings import *

DEBUG = False
ALLOWED_HOSTS = []
SECRET_KEY = os.environ.get("SECRET_KEY", SECRET_KEY)

# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Database - use PostgreSQL
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME"),
        "USER": os.environ.get("DB_USER"),
        "PASSWORD": os.environ.get("DB_PASSWORD"),
        "HOST": os.environ.get("DB_HOST"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}

# Redis
CELERY_BROKER_URL = os.environ.get("REDIS_URL")