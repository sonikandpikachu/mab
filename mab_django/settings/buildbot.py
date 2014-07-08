from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

INSTALLED_APPS += (
    'coverage',
    'django_coverage',
)

COVERAGE_MODULE_EXCLUDES = ['tests$', 'settings$', 'urls$', 'locale$',
    '__init__', 'django', 'migrations', 'south']


SECRET_KEY = '9v*1)^ixje!h8920_yf7cnb2d7e7!sv@bnm_fym1l)tr7&amp;fst&amp;'

DEBUG = True
TEMPLATE_DEBUG = DEBUG

SOUTH_TESTS_MIGRATE = False  # To disable migrations and use syncdb instead
SKIP_SOUTH_TESTS = True      # To disable South's own unit tests

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = join(PROJECT_ROOT, 'testmails/')
DEFAULT_FROM_EMAIL = 'webmaster@localhost'
