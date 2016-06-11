from django.conf.urls import patterns, url, include
from rest_framework import routers
from notifications import api
from notifications import views

router = routers.DefaultRouter()
router.register(r'municipality', api.MunicipalityViewSet)
router.register(r'district', api.DistrictViewSet)
router.register(r'districtexceptions', api.DistrictExceptionsViewSet)
router.register(r'addressblock', api.AddressBlockViewSet)
router.register(r'subscription', api.SubscriptionViewSet)


urlpatterns = [
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
    # urls for Municipality
    url(r'^municipality/$', views.MunicipalityListView.as_view(), name='app_name_municipality_list'),
    url(r'^municipality/create/$', views.MunicipalityCreateView.as_view(), name='app_name_municipality_create'),
    url(r'^municipality/detail/(?P<slug>\S+)/$', views.MunicipalityDetailView.as_view(), name='app_name_municipality_detail'),
    url(r'^municipality/update/(?P<slug>\S+)/$', views.MunicipalityUpdateView.as_view(), name='app_name_municipality_update'),
    # urls for District
    url(r'^district/$', views.DistrictListView.as_view(), name='app_name_district_list'),
    url(r'^district/create/$', views.DistrictCreateView.as_view(), name='app_name_district_create'),
    url(r'^district/detail/(?P<slug>\S+)/$', views.DistrictDetailView.as_view(), name='app_name_district_detail'),
    url(r'^district/update/(?P<slug>\S+)/$', views.DistrictUpdateView.as_view(), name='app_name_district_update'),
    # urls for DistrictExceptions
    url(r'^districtexceptions/$', views.DistrictExceptionsListView.as_view(), name='app_name_districtexceptions_list'),
    url(r'^districtexceptions/create/$', views.DistrictExceptionsCreateView.as_view(), name='app_name_districtexceptions_create'),
    url(r'^districtexceptions/detail/(?P<slug>\S+)/$', views.DistrictExceptionsDetailView.as_view(), name='app_name_districtexceptions_detail'),
    url(r'^districtexceptions/update/(?P<slug>\S+)/$', views.DistrictExceptionsUpdateView.as_view(), name='app_name_districtexceptions_update'),
    # urls for AddressBlock
    url(r'^addressblock/$', views.AddressBlockListView.as_view(), name='app_name_addressblock_list'),
    url(r'^addressblock/create/$', views.AddressBlockCreateView.as_view(), name='app_name_addressblock_create'),
    url(r'^addressblock/detail/(?P<slug>\S+)/$', views.AddressBlockDetailView.as_view(), name='app_name_addressblock_detail'),
    url(r'^addressblock/update/(?P<slug>\S+)/$', views.AddressBlockUpdateView.as_view(), name='app_name_addressblock_update'),
    # urls for Subscription
    url(r'^subscription/$', views.SubscriptionListView.as_view(), name='app_name_subscription_list'),
    url(r'^subscription/create/$', views.SubscriptionCreateView.as_view(), name='app_name_subscription_create'),
    url(r'^subscription/detail/(?P<slug>\S+)/$', views.SubscriptionDetailView.as_view(), name='app_name_subscription_detail'),
    url(r'^subscription/update/(?P<slug>\S+)/$', views.SubscriptionUpdateView.as_view(), name='app_name_subscription_update'),
]

