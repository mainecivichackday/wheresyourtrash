from django.conf.urls import url, include
from rest_framework import routers
import .api
import .views

router = routers.DefaultRouter()
router.register(r'provider', api.ProviderViewSet)


urlpatterns = [
    # urls for Django Rest Framework API
    url(r'^api/v1/', include(router.urls)),
]

urlpatterns += []


'''
# Basic CRUD urls ... not useds
urlpatterns += [
    url(r'^email2sms/provider/$', views.ProviderListView.as_view(), name='email2sms_provider_list'),
    url(r'^email2sms/provider/create/$', views.ProviderCreateView.as_view(), name='email2sms_provider_create'),
    url(r'^email2sms/provider/detail/(?P<slug>\S+)/$', views.ProviderDetailView.as_view(), name='email2sms_provider_detail'),
    url(r'^email2sms/provider/update/(?P<slug>\S+)/$', views.ProviderUpdateView.as_view(), name='email2sms_provider_update'),
]
'''

