# Uncomment the next two lines to enable the admin:
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, re_path
from django.urls import include
from django.views.generic import RedirectView

from rest_framework_swagger.views import get_swagger_view

from django.contrib import admin
admin.autodiscover()

schema_view = get_swagger_view(title="Test API")


urlpatterns = [
    path(r'session_security/', include('session_security.urls')),


    re_path(r'^$', RedirectView.as_view(url='/scores/test/', permanent=False), name='home'),

    # re_path(r'^users/', include('apps.users.urls')),
    re_path(r'^scores/', include('apps.scores.urls')),
    # re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    re_path(r'^rest-api/', schema_view),
    re_path(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    re_path(r'^admin/', admin.site.urls),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns