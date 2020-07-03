
DJANGO_APPS = (
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.messages',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.staticfiles',

)

THIRD_PARTY_APPS = (
    'django_admin_bootstrapped',
    'djangojs',
    'dajaxice',
    'dajax',

    'rest_framework',
    'rest_framework.authtoken',
    'rest_framework_swagger',

    'djangobower',
    'django_filters',
    'json_field',


    'debug_toolbar',


    'session_security',

    'datatableview',

    'django_select2',

    'axes',

    'push_notifications',


    "django_countries",

    "celery",
    'django_celery_beat',
    'bootstrap3_datetime',
    'datetimewidget',
    'djqscsv',
    'passwords',
    'nocaptcha_recaptcha',
    'simple_history',
    'django_extensions',
    'django_mysql'
)

LOCAL_APPS = (
    'apps.scores',

)

PASSWORD_MIN_LENGTH = 8
PASSWORD_COMPLEXITY = {"UPPER":  1, "LOWER":  1, "DIGITS": 1}


INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# from scores_start.external_module.apps import EXTERNAL_APPS_LIST
# INSTALLED_APPS = INSTALLED_APPS + EXTERNAL_APPS_LIST

PATIENT_IMPORT_PAYMENT_REF_PREFIX = "NWHB"

