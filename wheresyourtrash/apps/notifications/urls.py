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
    url(r'^$', views.MunicipalityListView.as_view(), name='home'),

    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
    # urls for Municipality
    url(r'^communities/$', views.MunicipalityListView.as_view(), name='municipality_list'),
    url(r'^communities/create/$', views.MunicipalityCreateView.as_view(), name='municipality_create'),
    url(r'^communities/(?P<slug>\S+)/$', views.MunicipalityDetailView.as_view(), name='municipality_detail'),
    url(r'^communities/update/(?P<slug>\S+)/$', views.MunicipalityUpdateView.as_view(), name='municipality_update'),
    # urls for District
    url(r'^district/$', views.DistrictListView.as_view(), name='district_list'),
    # urls for Subscription
    url(r'^subscriptions/$', views.SubscriptionListView.as_view(), name='subscription_list'),
    url(r'^subscriptions/create/$', views.SubscriptionCreateView.as_view(), name='subscription_create'),
    url(r'^subscriptions/(?P<pk>\S+)/$', views.SubscriptionDetailView.as_view(), name='subscription_detail'),
    url(r'^subscriptions/(?P<pk>\S+)/update/$', views.SubscriptionUpdateView.as_view(), name='subscription_update'),
]

