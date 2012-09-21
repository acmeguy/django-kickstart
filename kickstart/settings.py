# coding=utf-8

#
# Start configuration by declaring the debuging state
#
DEBUG = True
TEMPLATE_DEBUG = DEBUG

#
# Database connections
#
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
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'waffle.middleware.WaffleMiddleware',
    )



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
    #
    # Admin and admin extensions
    #
    # Madnatory placement for devserver, django-grapelli & filebrowser
    'devserver',
    'grappelli',
    'filebrowser',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'raven.contrib.django',
    #
    # Development Utilities
    #
    'django_extensions',
    'debug_toolbar',
    'waffle',
    'sorl.thumbnail',
    #
    # Utilities - applications/packages
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
INTERNAL_IPS = ('127.0.0.1',)

DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',

    # Modules not enabled by default
    'devserver.modules.ajax.AjaxDumpModule',
    #'devserver.modules.profile.MemoryUseModule',
    'devserver.modules.cache.CacheSummaryModule',
    'devserver.modules.profile.LineProfilerModule',
    )

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
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
    from local_settings import *
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
        EXTERNAL_SERVICES = merge(EXTERNAL_SERVICES,EXTERNAL_SERVICES_OVERRIDE)
    except Exception, e:
        pass

    try:
        EXTERNAL_STATIC_FILES = merge(EXTERNAL_STATIC_FILES,EXTERNAL_STATIC_FILES_OVERRIDE)
    except Exception, e:
        pass

    try:
        INDEXING_SERVICES = merge(INDEXING_SERVICES,INDEXING_SERVICES_OVERRIDE)
    except Exception, e:
        pass

    try:
        CACHES = merge(CACHES,CACHES_OVERRIDE)
    except Exception, e:
        pass

except Exception, e:
    import logging
    logging.warn('No local settings found... please use samples in the "configuration" directory for bootstrapping')
