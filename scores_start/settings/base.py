import os
from django.urls import reverse_lazy

PROJECT_NAME = 'Test Project'
PROJECT_APP_NAME = 'test'


ADMINS = [('Kiash', 'kiash.wisys@gmail.com')]

MANAGERS = ADMINS

HOST_IP_ADDRESS = os.environ.get('HOST_IP', None)

ALLOWED_HOSTS = [ '.clientdomain.com'] + ['192.168.0.101']

if HOST_IP_ADDRESS:
    ALLOWED_HOSTS += [HOST_IP_ADDRESS]

#TIME_ZONE = 'Asia/Dhaka'

######################################## LANGUAGE ################################################

LANGUAGE_CODE = 'en-us'

USE_I18N = True

USE_L10N = True

USE_TZ = True


SECRET_KEY = '=xjr+70(^1l71^%5lyf*#l0g!mb@^q(9gtk-*0lg@@_7z+5p+q'

# WSGI_APPLICATION = 'scores_start.wsgi.application'

MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

TEMPLATED_EMAIL_BACKEND = 'templated_email.backends.vanilla_django.TemplateBackend'

# TEST_RUNNER = 'apps.core.testing.DatabaselessTestRunner'

LANGUAGES = (
    ('en', 'English'),
)


DATE_INPUT_FORMATS = ('%d-%m-%Y', '%Y-%m-%d', '%m-%d-%Y','%d-%B-%Y',)

# AUTH_PROFILE_MODULE = 'users.Profile'
# ACCOUNT_ACTIVATION_DAYS = 7 # One-week activation window; you may, of course, use a different value.

#DEBUG

INTERNAL_IPS = ('127.0.0.1',)

# For Custom url after registration.
# ABSOLUTE_URL_OVERRIDES = {
#     'auth.user': lambda u: reverse_lazy('edit-profile'),
# }

SESSION_COOKIE_HTTPONLY = True
CSRF_COOKIE_HTTPONLY = True
#
# EXTRA_DATETIME_FORMATS = {
#     "year_short_month_name_day": "%Y-%b-%d"
# }
