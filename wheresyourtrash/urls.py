from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^', include('notifications.urls', namespace='notifications')),
]

if settings.DEBUG:
    import debug_toolbar
    from django.views.static import  serve
    urlpatterns.append(
        url(r'^media/(?P<path>.*)$', serve,  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))
    urlpatterns.append(
        url(r'^__debug__/', include(debug_toolbar.urls)))
