#/////////////////////////////////////////////////////////////////
import os 
#-----------------------------------------------------------------
from djangoappengine.settings_base import *
#-----------------------------------------------------------------

#/////////////////////////////////////////////////////////////////
ADMINS = (('Lightyblog', 'lightyblog@gmail.com'),)
MANAGERS = ADMINS

#/////////////////////////////////////////////////////////////////
# Activate django-dbindexer for the default database
DATABASES['default'] = {'ENGINE': 'dbindexer', 'TARGET': DATABASES['default']}
AUTOLOAD_SITECONF = 'indexes'

#/////////////////////////////////////////////////////////////////
# Get project directories
ROOT_DIR    = os.path.split(os.path.abspath(os.path.dirname(__file__)))[0]
PROJECT_DIR = os.path.abspath(os.path.dirname(__file__))

#/////////////////////////////////////////////////////////////////
# Login/Admin settings
LOGIN_REDIRECT_URL = '/admin/list-article'
LOGIN_URL = '/login/'
FORCE_SCRIPT_NAME = ''

#/////////////////////////////////////////////////////////////////
ALLOWED_HOSTS = ['high-hue-532.appspot.com']

TIME_ZONE = 'Europe/London'

#/////////////////////////////////////////////////////////////////
LANGUAGE_CODE = 'en-us'
USE_I18N = True
USE_L10N = True
USE_TZ = False
SITE_ID = 1

#/////////////////////////////////////////////////////////////////
MEDIA_ROOT = ''
MEDIA_URL = ''

#/////////////////////////////////////////////////////////////////
# Static files and paths
STATIC_ROOT = PROJECT_DIR + '/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    PROJECT_DIR + '/static/',
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

#/////////////////////////////////////////////////////////////////
# Secret random key
SECRET_KEY = '65f0$u^fa7i5k*no$(!6gsc!%s-#eea=o4-q$$@co5xz%zn79h'

#/////////////////////////////////////////////////////////////////
# Template loaders
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

#/////////////////////////////////////////////////////////////////
# Middlewares 
MIDDLEWARE_CLASSES = (
    # This loads the index definitions, so it has to come first
    'autoload.middleware.AutoloadMiddleware',

    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

#/////////////////////////////////////////////////////////////////
ROOT_URLCONF = 'lightyblog.urls'

#/////////////////////////////////////////////////////////////////
# Template directories
TEMPLATE_DIRS = (
    PROJECT_DIR + '/templates/',
)

#/////////////////////////////////////////////////////////////////
# APPS
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'djangotoolbox',
    'autoload',
    'dbindexer',
    'lightyblog',

    # djangoappengine should come last, so it can override a few manage.py commands
    'djangoappengine',
)

#/////////////////////////////////////////////////////////////////
# logging 
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
