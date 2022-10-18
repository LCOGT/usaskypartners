from .base import *
import ast
import sys
import os

ALLOWED_HOSTS = ['*']

WAGTAILADMIN_BASE_URL = "https://usaskypartners.lco.global"

DEBUG = ast.literal_eval(os.environ.get('DEBUG', 'False'))
if DEBUG:
    print('WARNING: DEBUG mode is turned on in PRODUCTION!', file=sys.stderr)

SECRET_KEY = os.environ['SECRET_KEY']

DATABASES = {
    'default': {
        'ENGINE': os.environ.get('DB_ENGINE', 'django.db.backends.postgresql'),
        'HOST': os.environ['DB_HOST'],
        'NAME': os.environ['DB_NAME'],
        'USER': os.environ['DB_USER'],
        'PASSWORD': os.environ['DB_PASS'],
        'OPTIONS': {
        },
    }
}

try:
    from .local import *
except ImportError:
    pass
