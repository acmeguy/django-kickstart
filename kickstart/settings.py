# coding=utf-8

#
# Start configuration by declaring the debuging state
#
DEBUG = True #todo - see local_settings.py for overrides
TEMPLATE_DEBUG = DEBUG
COMPRESS_ENABLED = False
NODEJS_FANOUT = False

#
# Database connections
#
DATABASES = {
    'default': {
        #'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'kickstart', # Or path to database file if using sqlite3.
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
SECRET_KEY = '9s#ve$^0@b1v)(_!%+e(o#ea&amp;@*h+5hrkuspb#y+4!$paya!_@' #todo - Make this unique, and don't share it with anybody.
ROOT_URLCONF = 'kickstart.urls'

ADMINS = (
    ('Kickstarter', 'kickstart@kickstart.com'), #todo replace this with you'r email
    )
MANAGERS = ADMINS

#
# Localization
#
TIME_ZONE       = 'Atlantic/Reykjavik'  #todo replace this with your timezone
LANGUAGE_CODE   = 'is-is'               #todo replace this with your locale
USE_I18N        = True
USE_L10N        = True
USE_TZ          = True
SKIN            = "kicktheme/"
LANGUAGES = (
    ('is', 'Icelandic'),
    ('en', 'English'),
    )

#
# Media files
#
MEDIA_ROOT = '/var/www/django/django-kickstart/media/' # Example: "/home/media/media.lawrence.com/media/" #todo replace this with your media root
MEDIA_URL = '' # Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
STATIC_ROOT = '/var/www/django/django-kickstart/static/' # Example: "/home/media/media.lawrence.com/static/"
STATIC_URL = '/static/' # Example: "http://media.lawrence.com/static/"

# Additional locations of static files
STATICFILES_DIRS = (
    # Example "/home/html/static" or "C:/www/django/static".
)
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
    )

#
#  Search - HAYSTACK - Solr
#
#

#Version 1.x
HAYSTACK_SEARCH_ENGINE = 'solr'
HAYSTACK_SITECONF = 'kickstart.search_confic'
HAYSTACK_SOLR_URL = 'http://192.168.1.103:8983/solr/kickstart'

#Version 2
#HAYSTACK_CONNECTIONS = {
#    'default': {
#        'ENGINE': 'haystack.backends.solr_backend.SolrEngine',
#        'URL': 'http://192.168.1.103:8983/solr/kickstart',
#        'TIMEOUT': 60 * 5,
#        'INCLUDE_SPELLING': True,
#        'BATCH_SIZE': 100,
#        #'EXCLUDED_INDEXES': ['thirdpartyapp.search_indexes.BarIndex'],
#    },
#}

#
# Templates
#


TEMPLATE_LOADERS = (
    ('django.template.loaders.cached.Loader', (
        'django.template.loaders.filesystem.Loader',
        'django.template.loaders.app_directories.Loader',
        )),
    )

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.debug',
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.i18n",
    'django.contrib.messages.context_processors.messages',
    'django.core.context_processors.request',
    'django.core.context_processors.static',
    'kickstart.web.context_processors.web_settings',
    )

COMPRESS_CSS_FILTERS = [
    'compressor.filters.css_default.CssAbsoluteFilter',
    #'compressor.filters.cssmin.CSSMinFilter',
]

#
# Middleware
#

MIDDLEWARE_CLASSES = (
    #
    # Caching
    #
    'django.middleware.cache.UpdateCacheMiddleware',
    #'django.middleware.cache.FetchFromCacheMiddleware',
    #'django.middleware.http.ConditionalGetMiddleware',
    #
    #
    #
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    #
    # Debugging and monitoring
    #
    'raven.contrib.django.middleware.Sentry404CatchMiddleware',
    'raven.contrib.django.middleware.SentryResponseErrorIdMiddleware',
    #'dogslow.WatchdogMiddleware',

    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware', #Clickjacking prevention

    'waffle.middleware.WaffleMiddleware',
    'django.middleware.gzip.GZipMiddleware',
    )

#
# Authentication & login
#
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'kickstart.KickstartUserProfile'


#EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'kickstart.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

INSTALLED_APPS = (
    #
    # Core Django applications
    #
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.webdesign',
    #
    # Admin and admin extensions
    #
    # Madnatory placement for devserver, django-grapelli & filebrowser
    'devserver',
    'grappelli',
    'djcelery',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'raven.contrib.django',
    'httpproxy',
    #
    # Development Utilities
    #
    'waffle',
    #
    # Utilities - applications/packages
    #
    'haystack',
    'redis_cache.stats',
    'tastypie',
    'crispy_forms',
    'rest_framework',
    'compressor',
    #
    # Kickstart - Application
    #
    #todo - change these according to your needs
    'kickstart',
    'kickstart.web',
    'kickstart.api',
    #
    #
    'userena',
    'easy_thumbnails',
    'guardian',
    #
    #
    'gunicorn',
    )



#
# Grappelli settings
#
GRAPPELLI_ADMIN_TITLE = 'Kickstart Admin'
AUTOCOMPLETE_LIMIT = 20


#
# API
#
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
    'PAGINATE_BY': 10,
    'FILTER_BACKEND': 'rest_framework.filters.DjangoFilterBackend',
}

#
# Caching
#
CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': '127.0.0.1:6379:1',
        'OPTIONS': {'DB': 1,},
    },
}

#
# Proxy
#
PROXY_DOMAIN = 'www.lorempixel.com'

"""
from dogpile.cache import make_region

region = make_region().configure(
    'dogpile.cache.redis',
    arguments = {
        'host': 'localhost',
        'port': 6379,
        'db':
        'redis_expiration_time': 60*60*2,   # 2 hours
        'distributed_lock':True
    }
)
"""

#
#
#
REDIS_CONNECT_RETRY             = True
REDIS_HOST                      = "localhost"
REDIS_PORT                      = 6379
REDIS_DB                        = "0"

BROKER_URL                      = 'redis://localhost:6379/0'
CELERY_SEND_EVENTS              = True
CELERY_RESULT_BACKEND           = "redis"
CELERY_TASK_RESULT_EXPIRES      = 25
CELERYD_CONCURRENCY             = 8
CELERYD_MAX_TASKS_PER_CHILD     = 10
CELERY_ALWAYS_EAGER             = False

SESSION_ENGINE                  = 'redis_sessions.session'
SESSION_REDIS_HOST              = 'localhost'
SESSION_REDIS_PORT              = 6379
SESSION_REDIS_DB                = 0
#SESSION_REDIS_PASSWORD         = 'password'
SESSION_REDIS_PREFIX            = 'session'

#
# Logging & Monitoring
#

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
        'handlers': ['sentry'],
        },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        },
    'handlers': {
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
            },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
            },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
            },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console'],
            'propagate': False,
            },
        },
    }

RAVEN_CONFIG = {
    'dsn': 'http://c606da0badfd4a2b9cea0e1c104a8248:1b1d01e94ddc4481940a1e69c17a684e@192.168.1.109:9000/2',
    'register_signals': True,
}


DOGSLOW = True # Watchdog is enabled by default, to temporarily disable, set to False:
DOGSLOW_OUTPUT = '/tmp' # Location where Watchdog stores its log files:
DOGSLOW_TIMER = 25 # Log requests taking longer than 25 seconds:
DOGSLOW_EMAIL_TO = 'stebax@gmail.com' # When both specified, emails backtraces:
DOGSLOW_EMAIL_FROM = 'stebax@gmail.com'
DOGSLOW_LOGGER = 'sentry.errors' # Also log to this logger (defaults to none):
DOGSLOW_LOG_LEVEL = 'WARNING'
DOGSLOW_STACK_VARS = False # can become huge if set to true
#DOGSLOW_IGNORE_URLS = ('some_view', 'other_view') # Tuple of url pattern names that should not be monitored:

#
# Integration With Local Settings
#

USE_LOCAL_FILE = True
#USE_LOCAL_FILE uses True by default but can be set to false to ignore local settings and testing production settings


try:
    from .local_settings import *
    from .utils.merge import merge

    if USE_LOCAL_FILE:
        try:
            INSTALLED_APPS = INSTALLED_APPS + LOCAL_INSTALLED_APPS
        except Exception, e:
            pass

        try:
            TEMPLATE_DIRS = TEMPLATE_DIRS + LOCAL_TEMPLATE_DIRS
        except Exception, e :
            pass

        try:
            MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + LOCAL_MIDDLEWARE_CLASSES
        except Exception, e :
            pass

        try:
            LOGGING = merge(LOGGING,LOCAL_LOG_OVERRIDE)
        except Exception, e:
            #print 'No local log settings found, is this production?'
            pass


        try:
            CACHES = merge(CACHES,LOCAL_CACHES)
        except Exception, e:
            pass

except Exception, e:
    import logging
    logging.warn('No local settings found... please use samples in the "configuration" directory for bootstrapping')
