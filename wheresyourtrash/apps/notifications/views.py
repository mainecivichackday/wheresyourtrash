from django.views.generic import FormView, DetailView, ListView, UpdateView, CreateView, TemplateView
from .models import Municipality, District, DistrictExceptions, AddressBlock, Subscription
from .forms import MunicipalityForm, DistrictForm, DistrictExceptionsForm, AddressBlockForm, SubscriptionForm



class HomeView(TemplateView):
    template_name="home.html"

class MunicipalityListView(ListView):
    model = Municipality


class MunicipalityCreateView(CreateView):
    model = Municipality
    form_class = MunicipalityForm


class MunicipalityDetailView(DetailView):
    model = Municipality

class MunicipalityUpdateView(UpdateView):
    model = Municipality
    form_class = MunicipalityForm


class DistrictListView(ListView):
    model = District


class DistrictCreateView(CreateView):
    model = District
    form_class = DistrictForm


class DistrictDetailView(DetailView):
    model = District


class DistrictUpdateView(UpdateView):
    model = District
    form_class = DistrictForm


class DistrictExceptionsListView(ListView):
    model = DistrictExceptions


class DistrictExceptionsCreateView(CreateView):
    model = DistrictExceptions
    form_class = DistrictExceptionsForm


class DistrictExceptionsDetailView(DetailView):
    model = DistrictExceptions


class DistrictExceptionsUpdateView(UpdateView):
    model = DistrictExceptions
    form_class = DistrictExceptionsForm


class AddressBlockListView(ListView):
    model = AddressBlock


class AddressBlockCreateView(CreateView):
    model = AddressBlock
    form_class = AddressBlockForm


class AddressBlockDetailView(DetailView):
    model = AddressBlock


class AddressBlockUpdateView(UpdateView):
    model = AddressBlock
    form_class = AddressBlockForm


class SubscriptionListView(ListView):
    model = Subscription


class SubscriptionCreateView(CreateView):
    model = Subscription
    form_class = SubscriptionForm


class SubscriptionDetailView(DetailView):
    model = Subscription


class SubscriptionUpdateView(UpdateView):
    model = Subscription
    form_class = SubscriptionForm

