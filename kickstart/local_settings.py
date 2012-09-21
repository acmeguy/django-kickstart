# coding=utf-8
# I use local_settings to host development settings so that the main settings file
# always represents a production state. Values here are merged with the main settings file.
# Settings can be replace all together, using the same variable names as in settings.py, or merged using the LOCAL_ prefix.

DEBUG = True
TEMPLATE_DEBUG = DEBUG
IS_DEVELOPMENT = True

DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.sqlite3', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kickstart_db', # Or path to database file if using sqlite3.
        'USER': 'kickstart', # Not used with sqlite3.
        'PASSWORD': 'kickstart', # Not used with sqlite3.
        'HOST': 'localhost', # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '', # Set to empty string for default. Not used with sqlite3.
    }
}

LOCAL_INSTALLED_APPS = (
    'devserver',
    )

LOCAL_MIDDLEWARE_CLASSES = (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    )

LOCAL_CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
        }
}
