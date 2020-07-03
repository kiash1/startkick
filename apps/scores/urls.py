
from django.contrib import admin
from django.urls import re_path
from rest_framework.urlpatterns import format_suffix_patterns
from apps.scores.api.views import *


admin.autodiscover()

urlpatterns = [

                       ########################################## API START ##############################################
                       re_path(r'^test/', hello_world, name='hello'),

                       ]

urlpatterns = format_suffix_patterns(urlpatterns)