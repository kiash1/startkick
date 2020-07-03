import os.path
from django.urls import reverse_lazy


PROJECT_ROOT = os.path.abspath('./')
PROJECT_BASE = os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../')
APPS_ROOT = os.path.abspath('./apps')

YOUR_CUSTOM_SETTING = 'some value'
SITE_ID = 1
SITE_URL = 'clienturl.com'
SITE_NAME = 'scores'
SITE_DOMAIN = 'clienturl.com'

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')


#SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTOCOL', 'https')


# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/var/www/example.com/media/"
MEDIA_ROOT = PROJECT_ROOT + "/media/"

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://example.com/media/", "http://media.example.com/"
MEDIA_URL = '/media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/var/www/example.com/static/"
STATIC_ROOT = PROJECT_ROOT + "/static/"

# URL prefix for static files.
# Example: "http://example.com/static/", "http://static.example.com/"
STATIC_URL = '/static/'

# for demo purpose
LOGIN_URL = reverse_lazy('lm_auth:lm_users_login')

LOGIN_REDIRECT_URL = reverse_lazy('user-landing')
LOGOUT_REDIRECT_URL = reverse_lazy("lm_auth:lm_users_login")
LOGOUT_URL = reverse_lazy('logout')

__TEMPLATE_DIRS = (
    os.path.join(PROJECT_BASE, 'templates'),
)

ROOT_URLCONF = 'scores_start.urls'

# Additional locations of static files
STATICFILES_DIRS = (
# Put strings here, like "/home/html/static" or "C:/www/django/static".
# Always use forward slashes, even on Windows.
# Don't forget to use absolute paths, not relative paths.

)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'djangobower.finders.BowerFinder',
    'dajaxice.finders.DajaxiceFinder',
    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django_jinja.loaders.AppLoader',
    'django_jinja.loaders.FileSystemLoader',
    'django.template.loaders.cached.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = [
    'django.contrib.auth.context_processors.auth',
    'django.template.context_processors.debug',
    'django.template.context_processors.i18n',
    'django.template.context_processors.media',
    'django.template.context_processors.static',
    'django.template.context_processors.tz',
    'django.template.context_processors.request',
    'django.contrib.messages.context_processors.messages',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': __TEMPLATE_DIRS,
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': TEMPLATE_CONTEXT_PROCESSORS,
            'libraries': {

            }
        },
    }
    ]
__MIDDLEWARE_CLASSES = [
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    # 'axes.middleware.FailedLoginMiddleware',
    #'python.path.to.LoginRequiredMiddleware',
    # 'session_security.middleware.SessionSecurityMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'session_security.middleware.SessionSecurityMiddleware',
    'simple_history.middleware.HistoryRequestMiddleware',

]




MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
] + __MIDDLEWARE_CLASSES


DEBUG_TOOLBAR_CONFIG = {
        'INTERCEPT_REDIRECTS': True,
    }
