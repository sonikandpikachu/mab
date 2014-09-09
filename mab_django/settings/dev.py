from .base import *


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mab',
        'USER': 'mabuser',
        'PASSWORD': 'mabpassword',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

INSTALLED_APPS += (
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',

    'coverage',
    'django_coverage',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

SECRET_KEY = '9v*1)^ixje!h8920_yf7cnb2d7e7!sv@bnm_fym1l)tr7&amp;fst&amp;'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SOUTH_TESTS_MIGRATE = False  # To disable migrations and use syncdb instead
SKIP_SOUTH_TESTS = True      # To disable South's own unit tests

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = join(PROJECT_ROOT, 'mails/')
DEFAULT_FROM_EMAIL = 'webmaster@localhost'

CORS_ORIGIN_ALLOW_ALL = True
