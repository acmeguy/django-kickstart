# coding=utf-8

#
# Start configuration by declaring the debuging state
#
DEBUG = False #todo - see local_settings.py for overrides
TEMPLATE_DEBUG = DEBUG

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
TIME_ZONE = 'Atlantic/Reykjavik' #todo replace this with your timezone
LANGUAGE_CODE = 'is-is'          #todo replace this with your locale
USE_I18N = True
USE_L10N = True
USE_TZ = True

#
# Media files
#
MEDIA_ROOT = '/var/www/django/kickstart/media/' # Example: "/home/media/media.lawrence.com/media/" #todo replace this with your media root
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
    'waffle.middleware.WaffleMiddleware',
    )

#
# Authentication & login
#
AUTHENTICATION_BACKENDS = (
    'userena.backends.UserenaAuthenticationBackend',
    'guardian.backends.ObjectPermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
    )

LOGIN_REDIRECT_URL = '/accounts/%(username)s/'
LOGIN_URL = '/accounts/signin/'
LOGOUT_URL = '/accounts/signout/'
ANONYMOUS_USER_ID = -1

AUTH_PROFILE_MODULE = 'kickstart.KickstartUserProfile'


EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

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
    #
    # Development Utilities
    #
    'waffle',
    #
    # Utilities - applications/packages
    #
    'redis_cache.stats',
    'tastypie',
    'crispy_forms',
    'userena',
    'guardian',
    'easy_thumbnails',
    #
    # Kickstart - Application
    #
    #todo - change these according to your needs
    'kickstart',
    'kickstart.web',
    )

#
# Grappelli settings
#
GRAPPELLI_ADMIN_TITLE = 'Kickstart Admin'
AUTOCOMPLETE_LIMIT = 20


#
# Caching
#

CACHES = {
    'default': {
        'BACKEND': 'redis_cache.cache.RedisCache',
        'LOCATION': 'localhost:6379',
        'OPTIONS': {'DB': 1,},
    },
}

"""
from dogpile.cache import make_region

region = make_region().configure(
    'dogpile.cache.redis',
    arguments = {
        'host': 'localhost',
        'port': 6379,
        'db': 0,
        'redis_expiration_time': 60*60*2,   # 2 hours
        'distributed_lock':True
    }
)
"""

#
#
#
BROKER_BACKEND                  = "redis"
BROKER_HOST                     = "localhost"
BROKER_PORT                     = 6379
BROKER_VHOST                    = "1"

REDIS_CONNECT_RETRY             = True
REDIS_HOST                      = "localhost"
REDIS_PORT                      = 6379
REDIS_DB                        = "0"

CELERY_SEND_EVENTS              = True
CELERYD_LOG_LEVEL               = 'INFO'
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
# Logging
#

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

SENTRY_DSN = 'SENTRY_DSN' #todo replace this with a real sentry dns string

#
# Integration With Local Settings
#

try:
    from .local_settings import *
    from .utils.merge import merge

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
