from django.conf.urls import patterns, url, include
from rest_framework import routers
import api
import views

router = routers.DefaultRouter()
router.register(r'municipality', api.MunicipalityViewSet)
router.register(r'district', api.DistrictViewSet)
router.register(r'districtexceptions', api.DistrictExceptionsViewSet)
router.register(r'addressblock', api.AddressBlockViewSet)
router.register(r'subscription', api.SubscriptionViewSet)


urlpatterns = patterns('',
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
)

urlpatterns += patterns('',
    # urls for Municipality
    url(r'^app_name/municipality/$', views.MunicipalityListView.as_view(), name='app_name_municipality_list'),
    url(r'^app_name/municipality/create/$', views.MunicipalityCreateView.as_view(), name='app_name_municipality_create'),
    url(r'^app_name/municipality/detail/(?P<slug>\S+)/$', views.MunicipalityDetailView.as_view(), name='app_name_municipality_detail'),
    url(r'^app_name/municipality/update/(?P<slug>\S+)/$', views.MunicipalityUpdateView.as_view(), name='app_name_municipality_update'),
)

urlpatterns += patterns('',
    # urls for District
    url(r'^app_name/district/$', views.DistrictListView.as_view(), name='app_name_district_list'),
    url(r'^app_name/district/create/$', views.DistrictCreateView.as_view(), name='app_name_district_create'),
    url(r'^app_name/district/detail/(?P<slug>\S+)/$', views.DistrictDetailView.as_view(), name='app_name_district_detail'),
    url(r'^app_name/district/update/(?P<slug>\S+)/$', views.DistrictUpdateView.as_view(), name='app_name_district_update'),
)

urlpatterns += patterns('',
    # urls for DistrictExceptions
    url(r'^app_name/districtexceptions/$', views.DistrictExceptionsListView.as_view(), name='app_name_districtexceptions_list'),
    url(r'^app_name/districtexceptions/create/$', views.DistrictExceptionsCreateView.as_view(), name='app_name_districtexceptions_create'),
    url(r'^app_name/districtexceptions/detail/(?P<slug>\S+)/$', views.DistrictExceptionsDetailView.as_view(), name='app_name_districtexceptions_detail'),
    url(r'^app_name/districtexceptions/update/(?P<slug>\S+)/$', views.DistrictExceptionsUpdateView.as_view(), name='app_name_districtexceptions_update'),
)

urlpatterns += patterns('',
    # urls for AddressBlock
    url(r'^app_name/addressblock/$', views.AddressBlockListView.as_view(), name='app_name_addressblock_list'),
    url(r'^app_name/addressblock/create/$', views.AddressBlockCreateView.as_view(), name='app_name_addressblock_create'),
    url(r'^app_name/addressblock/detail/(?P<slug>\S+)/$', views.AddressBlockDetailView.as_view(), name='app_name_addressblock_detail'),
    url(r'^app_name/addressblock/update/(?P<slug>\S+)/$', views.AddressBlockUpdateView.as_view(), name='app_name_addressblock_update'),
)

urlpatterns += patterns('',
    # urls for Subscription
    url(r'^app_name/subscription/$', views.SubscriptionListView.as_view(), name='app_name_subscription_list'),
    url(r'^app_name/subscription/create/$', views.SubscriptionCreateView.as_view(), name='app_name_subscription_create'),
    url(r'^app_name/subscription/detail/(?P<slug>\S+)/$', views.SubscriptionDetailView.as_view(), name='app_name_subscription_detail'),
    url(r'^app_name/subscription/update/(?P<slug>\S+)/$', views.SubscriptionUpdateView.as_view(), name='app_name_subscription_update'),
)

