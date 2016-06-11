import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from .models import Provider
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType


def create_django_contrib_auth_models_user(**kwargs):
    defaults = {}
    defaults["username"] = "username"
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_provider(**kwargs):
    defaults = {}
    defaults["name"] = "name"
    defaults["email_root"] = "email_root"
    defaults.update(**kwargs)
    return Provider.objects.create(**defaults)


class ProviderViewTest(unittest.TestCase):
    '''
    Tests for Provider
    '''
    def setUp(self):
        self.client = Client()

    def test_list_provider(self):
        url = reverse('email2sms_provider_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_provider(self):
        url = reverse('email2sms_provider_create')
        data = {
            "name": "name",
            "email_root": "email_root",
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_provider(self):
        provider = create_provider()
        url = reverse('email2sms_provider_detail', args=[provider.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_update_provider(self):
        provider = create_provider()
        data = {
            "name": "name",
            "email_root": "email_root",
        }
        url = reverse('email2sms_provider_update', args=[provider.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


