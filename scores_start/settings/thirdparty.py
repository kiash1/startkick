import os
from django.conf import settings
################################ SESSION SECURITY ################################################

SESSION_SECURITY_EXPIRE_AFTER=600
SESSION_SECURITY_WARN_AFTER=300

################################## DEBUG_TOOLBAR  ################################################

DEBUG_TOOLBAR_PANELS = [
    'debug_toolbar.panels.versions.VersionsPanel',
    'debug_toolbar.panels.timer.TimerPanel',
    'debug_toolbar.panels.settings.SettingsPanel',
    'debug_toolbar.panels.headers.HeadersPanel',
    'debug_toolbar.panels.request.RequestPanel',
    'debug_toolbar.panels.sql.SQLPanel',
    'debug_toolbar.panels.staticfiles.StaticFilesPanel',
    'debug_toolbar.panels.templates.TemplatesPanel',
    'debug_toolbar.panels.cache.CachePanel',
    'debug_toolbar.panels.signals.SignalsPanel',
    'debug_toolbar.panels.logging.LoggingPanel',
    'debug_toolbar.panels.redirects.RedirectsPanel',
]

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

###################################### AXES ################################################

AXES_LOGIN_FAILURE_LIMIT = 3
#AXES_LOCKOUT_TEMPLATE = "users/lockout.html"
AXES_LOCKOUT_TEMPLATE = "users/lockout-mobilemed.html"
AXES_LOCK_OUT_AT_FAILURE = True
AXES_LOCK_OUT_BY_COMBINATION_USER_AND_IP = True

###################################### SWAGGER ################################################


SWAGGER_SETTINGS = {
    "exclude_namespaces": [], # List URL namespaces to ignore
    "api_version": '0.1', # Specify your API's version
    "api_path": "/", # Specify the path to your API not a root level
    "enabled_methods": [# Specify which methods to enable in Swagger UI
                        'get',
                        'post',
                        'put',
                        'patch',
                        'delete'
    ],
    "api_key": '', # An API key
    "is_authenticated": False, # Set to True to enforce user authentication,
    "is_superuser": True, # Set to True to enforce admin only access
}

######################################## BOWER ################################################

from scores_start.settings import PROJECT_ROOT

BOWER_COMPONENTS_ROOT = PROJECT_ROOT
BOWER_INSTALLED_APPS = (
    'bootstrap#2.3.2',
    'jquery#1.9.1',
    'bootstrap-datetimepicker',
    'bootstrap-timepicker',
    'datatables',
    'noty',
    'zoomooz',
    'highcharts',
    'bootstrap-tagsinput',
    'select2',
    'jasny-bootstrap',
    'jquery.cookie',
    'Avgrund',
    #'multiple-select',
    'git://github.com/milu-buet/multiple-select.git',
    'jquery.validation',
    'https://github.com/davetayls/jquery.kinetic.git',
    'https://github.com/ibrahim12/jquery-powertip.git#release',
    #'https://github.com/ibrahim12/Messi.git',
    'https://github.com/milu-buet/Messi.git',
    'https://github.com/atkinson/jquery-django-messages.git',
    'https://github.com/vitalets/x-editable.git#1.5.0',
    'https://github.com/nostalgiaz/bootstrap-switch.git#2.0.1',
    #'https://github.com/pivotal-energy-solutions/django-datatable-view.git',
    # 'https://github.com/milu-buet/django-datatable-view.git',
    'vis',

)


######################################## REST FRAMEWORK ################################################

REST_FRAMEWORK = {

    # 'DEFAULT_RENDERER_CLASSES': (
    #     'rest_framework_csv.renderers.CSVRenderer',
    # ),

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',

    ),
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.JSONParser',
    ),

    # Use hyperlinked styles by default.
    # Only used if the `serializer_class` attribute is not set on a view.
    'DEFAULT_MODEL_SERIALIZER_CLASS':
        'rest_framework.serializers.ModelSerializer',

    'DEFAULT_FILTER_BACKENDS':
        ('rest_framework.filters.OrderingFilter',),



    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    # 'DEFAULT_PERMISSION_CLASSES': [
    # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    # ],

    'PAGINATE_BY': 5, # Default to 10
    'PAGINATE_BY_PARAM': 'page_size', # Allow client to override, using `?page_size=xxx`.
    'MAX_PAGINATE_BY': 100 # Maximum limit allowed when using `?page_size=xxx`.
}

######################################## DAJAXICE ########################################################

DAJAXICE_MEDIA_PREFIX = "dajaxice"


######################################## PUSH NOTIFICATION ################################################



####################################### Celery Start##############################################
from celery.schedules import crontab

CELERY_TIME_ZONE = 'UTC'
CELERY_ENABLE_UTC = False
CELERY_TASK_ALWAYS_EAGER = False
CELERYD_TASK_TIME_LIMIT = 300
CELERY_ACCEPT_CONTENT = ['pickle', 'json']

CELERY_BEAT_SCHEDULE = {

}

''' Note: To Find out other beat schedule task search for **setup_periodic_tasks** functions definitions'''
# TODO keep all schdeuled tasks in a single place

####################################### Celery End##############################################

DJANGO_SIMPLE_HISTORY_ACTIVATED = True

# for capthca configuration
NOR_SITE_KEY = os.environ.get('NOR_SITE_KEY' , None)
NORECAPTCHA_SITE_KEY = NOR_SITE_KEY

NOR_SECRET_KEY = os.environ.get('NOR_SECRET_KEY' , None)
NORECAPTCHA_SECRET_KEY = NOR_SECRET_KEY

SOUTH_MIGRATION_MODULES = {
    "push_notifications": "push_notifications.south_migrations"
}

# instance specific email configuration json file path
