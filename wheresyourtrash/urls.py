from django.conf import settings
from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from rest_framework import routers

from django.contrib import admin
admin.autodiscover()

from email2sms.api import ProviderViewSet
from notifications.api import *

router = routers.DefaultRouter()
router.register(r'provider', ProviderViewSet)
router.register(r'municipality', MunicipalityViewSet)
router.register(r'district', DistrictViewSet)
router.register(r'districtexceptions', DistrictExceptionsViewSet)
router.register(r'addressblock', AddressBlockViewSet)
router.register(r'subscription', SubscriptionViewSet)

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/v1/', include(router.urls)),
    url(r'^', include('email2sms.urls', namespace='email2sms')),
    url(r'^', include('notifications.urls', namespace='notifications')),
]

if settings.DEBUG:
    try:
        import debug_toolbar
        urlpatterns.append(
            url(r'^__debug__/', include(debug_toolbar.urls)))
    except ImportError:
        # Skip adding debug toolbar for now
        pass
    from django.views.static import  serve
    urlpatterns.append(
        url(r'^media/(?P<path>.*)$', serve,  # NOQA
            {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}))
    urlpatterns.append(
        url(r'^static/(?P<path>.*)$',serve,{'document_root': settings.STATIC_ROOT}))
