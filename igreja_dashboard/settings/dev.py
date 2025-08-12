from .base import *  # noqa
import os
import dj_database_url  # type: ignore

DEBUG = True

# Permite usar DATABASE_URL no dev, caindo para SQLite por padrão
DATABASE_URL = os.environ.get('DATABASE_URL')
if DATABASE_URL:
    DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=0)
else:
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }

# Emails em console no dev (padrão), pode ser sobrescrito via env
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')