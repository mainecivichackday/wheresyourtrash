from django.contrib import messages
from django.views.generic import DetailView, ListView, UpdateView, CreateView, TemplateView
from django.core.urlresolvers import reverse

from .models import Municipality, District, DistrictExceptions, AddressBlock, Subscription
from .forms import MunicipalityForm, DistrictForm, DistrictExceptionsForm, AddressBlockForm, SubscriptionForm

from braces.views import LoginRequiredMixin


class HomeView(TemplateView):
    template_name="home.html"

class MunicipalityListView(ListView):
    model = Municipality


class MunicipalityCreateView(CreateView):
    model = Municipality
    form_class = MunicipalityForm


class MunicipalityDetailView(DetailView):
    model = Municipality

    def subscription_form(self):
        choices = [(d.id, d.name) for d in District.objects.filter(municipality=self.object)]
        form = SubscriptionForm(initial={'user':self.request.user})
        form.fields['district'].choices = choices
        return form

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


class SubscriptionMixin(object):
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Subscription.objects.filter(user=self.request.user)
        else:
            return Subscription.objects.none()


class SubscriptionListView(SubscriptionMixin, ListView):
    model = Subscription


class SubscriptionCreateView(SubscriptionMixin, LoginRequiredMixin, CreateView):
    model = Subscription
    form_class = SubscriptionForm

    def get_initial(self):
        """
        Returns the initial data to use for forms on this view.
        """
        initial = super(SubscriptionCreateView, self).get_initial()
        initial['user'] = self.request.user
        return initial


    def get_success_url(self):
        return reverse('notifications:subscription_list')

class SubscriptionDetailView(SubscriptionMixin, LoginRequiredMixin, DetailView):
    model = Subscription


class SubscriptionUpdateView(SubscriptionMixin, LoginRequiredMixin, UpdateView):
    model = Subscription
    form_class = SubscriptionForm
