from django.conf.urls import url
from django.views.generic import TemplateView

from .views import (MunicipalityDetailView, MunicipalityListView,
                    District)
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="homepage.html"),
        name="search"),
    url(r'^municipalites/([\w-]+)/signup$', MunicipalitySignupView.as_view(),
        name='municipality-signup'),
    url(r'^municipalites/([\w-]+)/$', MunicipalityDetailView.as_view(),
        name='municipality-detail'),
    url(r'^municipalites/$', MunicipalityListView.as_view(),
        name="municipality-list")
]
