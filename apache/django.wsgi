import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/Users/zss/.virtualenvs/mhealthprojectenv/lib/python2.7/site-packages')

# Add the app's directory to the PYTHONPATH
sys.path.append('/Users/zss/django_projects/officialProjects')
sys.path.append('/Users/zss/django_projects/officialProjects/mhealth_web')

os.environ['DJANGO_SETTINGS_MODULE'] = 'scores_start.settings'

# Activate your virtual env
activate_env=os.path.expanduser("/Users/zss/.virtualenvs/mhealthprojectenv/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()