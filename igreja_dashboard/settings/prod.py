from .base import *  # noqa
import os
import dj_database_url  # type: ignore

DEBUG = False

# Segurança básica para prod — pode ser controlada por env
SECURE_SSL_REDIRECT = os.environ.get('SECURE_SSL_REDIRECT', 'True').lower() in ('true', '1', 'yes')
SESSION_COOKIE_SECURE = os.environ.get('SESSION_COOKIE_SECURE', 'True').lower() in ('true', '1', 'yes')
CSRF_COOKIE_SECURE = os.environ.get('CSRF_COOKIE_SECURE', 'True').lower() in ('true', '1', 'yes')
SECURE_HSTS_SECONDS = int(os.environ.get('SECURE_HSTS_SECONDS', '31536000'))
SECURE_HSTS_INCLUDE_SUBDOMAINS = os.environ.get('SECURE_HSTS_INCLUDE_SUBDOMAINS', 'True').lower() in ('true', '1', 'yes')
SECURE_HSTS_PRELOAD = os.environ.get('SECURE_HSTS_PRELOAD', 'True').lower() in ('true', '1', 'yes')

# Whitenoise para servir estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Database via env (obrigatório em prod)
DATABASE_URL = os.environ.get('DATABASE_URL')
if not DATABASE_URL:
    raise ValueError('DATABASE_URL deve estar definida no ambiente de produção')
DATABASES['default'] = dj_database_url.parse(DATABASE_URL, conn_max_age=600)