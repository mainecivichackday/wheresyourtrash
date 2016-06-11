from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import Provider
from .forms import ProviderForm


'''
class ProviderListView(ListView):
    model = Provider


class ProviderCreateView(CreateView):
    model = Provider
    form_class = ProviderForm


class ProviderDetailView(DetailView):
    model = Provider


class ProviderUpdateView(UpdateView):
    model = Provider
    form_class = ProviderForm
'''
