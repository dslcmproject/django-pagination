import sys

from django.conf import settings

settings.configure(DEBUG=True,
                   DATABASES={
                       'default': {
                           'ENGINE': 'django.db.backends.sqlite3',
                       }
                   },
                   ROOT_URLCONF='',
                   INSTALLED_APPS=('django.contrib.auth',
                                   'django.contrib.contenttypes',
                                   'django.contrib.sessions',
                                   'django.contrib.admin',
                                   'pagination',),
                   MIDDLEWARE=(),
                   TEMPLATES = [
                       {
                           'BACKEND': 'django.template.backends.django.DjangoTemplates',
                           'DIRS': [],
                           'APP_DIRS': True,
                           'OPTIONS': {
                               # ... some options here ...
                               },
                           },
                       ]
                   )

import django
django.setup()

if __name__ == "__main__":
    try:
        # Django <= 1.8
        from django.test.simple import DjangoTestSuiteRunner
        test_runner = DjangoTestSuiteRunner(verbosity=1)
    except ImportError:
        # Django >= 1.8
        from django.test.runner import DiscoverRunner
        test_runner = DiscoverRunner(verbosity=1)

    failures = test_runner.run_tests(['pagination'])
    if failures:
        sys.exit(failures)
