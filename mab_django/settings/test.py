""" Test settings and globals which allow us to run our test suite locally. """
from .dev import *


IS_TEST = True

TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
TEST_DISCOVER_TOP_LEVEL = PROJECT_ROOT
TEST_DISCOVER_ROOT = PROJECT_ROOT

NOSE_ARGS = [
    '--cover-package=mab_django',
    '--verbosity=2',
]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    },
}

MEDIA_ROOT = join(PROJECT_ROOT, 'testmedia')
EMAIL_FILE_PATH = join(PROJECT_ROOT, 'test_mails/')

import logging
logging.disable(logging.CRITICAL)

# # Remove debug_toolbar from testing
# INSTALLED_APPS = list(INSTALLED_APPS)
# del INSTALLED_APPS['debug_toolbar']
# MIDDLEWARE_CLASSES = list(MIDDLEWARE_CLASSES)
# del MIDDLEWARE_CLASSES['debug_toolbar.middleware.DebugToolbarMiddleware']
