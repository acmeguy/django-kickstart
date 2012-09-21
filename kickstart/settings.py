# Django settings for django_kickstart project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Kickstarter', 'kickstart@kickstart.com'),
)

MANAGERS = ADMINS

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

#
# Site setup
#
SITE_ID = 1
SECRET_KEY = '9s#ve$^0@b1v)(_!%+e(o#ea&amp;@*h+5hrkuspb#y+4!$paya!_@' # Make this unique, and don't share it with anybody.
ROOT_URLCONF = 'kickstart.urls'

#
# Localization
#
TIME_ZONE = 'Atlantic/Reykjavik'
LANGUAGE_CODE = 'is-is'
USE_I18N = True
USE_L10N = True
USE_TZ = True

#
# Media files
#
MEDIA_ROOT = '/var/www/django/kickstart/media/' # Example: "/home/media/media.lawrence.com/media/"
MEDIA_URL = '' # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
STATIC_ROOT = '' # Example: "/home/media/media.lawrence.com/static/"
STATIC_URL = '/static/' # Example: "http://media.lawrence.com/static/"

# Additional locations of static files
STATICFILES_DIRS = (
# Example "/home/html/static" or "C:/www/django/static".
)
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    )

#
# Templates
#

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    )

#
# Middleware
#

MIDDLEWARE_CLASSES = (
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', #Clickjacking prevention
    'django.middleware.cache.FetchFromCacheMiddleware',

    )



# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'kickstart.wsgi.application'

TEMPLATE_DIRS = (
# Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #
    # Admin
    #
    # Madnatory placement for devserver, django-grapelli & filebrowser
    'devserver',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    #
    # Utils
    #
    'tastypie',
    'crispy_forms',
    #
    # Kickstart - Application
    #

    )

#
# Grappelli settings
#
GRAPPELLI_ADMIN_TITLE = 'Kickstart Admin'
AUTOCOMPLETE_LIMIT = 20

#
# Development settings
#

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.profile.LineProfilerModule',
    )

#
# Caching
#

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
