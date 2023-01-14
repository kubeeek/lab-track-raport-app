from .settings import *

SOUTH_TESTS_MIGRATE = False
DATABASES['default'] = {'ENGINE': 'django.db.backends.sqlite3'}
DATABASES['default']['NAME'] = ':memory:'