import unittest
from django.core.urlresolvers import reverse
from django.test import Client
from notifications.models import Municipality, District, DistrictExceptions, AddressBlock, Subscription
from custom_user.models import EmailUser as User
from django.contrib.auth.models import Group
from django.contrib.contenttypes.models import ContentType
from datetime import datetime


def create_user(**kwargs):
    defaults = {}
    defaults["email"] = "username@tempurl.com"
    defaults.update(**kwargs)
    return User.objects.get_or_create(**defaults)[0]


def create_django_contrib_auth_models_group(**kwargs):
    defaults = {}
    defaults["name"] = "group"
    defaults.update(**kwargs)
    return Group.objects.get_or_create(**defaults)


def create_django_contrib_contenttypes_models_contenttype(**kwargs):
    defaults = {}
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_municipality(**kwargs):
    defaults = {}
    defaults["slug"] = "bangor"
    defaults["name"] = "Bangor"
    defaults["updated"] = datetime.now()
    defaults["state"] = "ME"
    defaults["population"] = 30000
    defaults["approved"] = "approved"
    defaults.update(**kwargs)
    #if "contacts" not in defaults:
    #    defaults["contacts"] = create_user()
    return Municipality.objects.get_or_create(**defaults)[0]


def create_district(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["name"] = "name"
    defaults["updated"] = "updated"
    defaults["trashed"] = "trashed"
    defaults["district_type"] = "district_type"
    defaults["pickup_time"] = "pickup_time"
    defaults.update(**kwargs)
    if "municipality" not in defaults:
        defaults["municipality"] = create_municipality()
    return District.objects.create(**defaults)


def create_districtexceptions(**kwargs):
    defaults = {}
    defaults["slug"] = "slug"
    defaults["name"] = "name"
    defaults["updated"] = "updated"
    defaults["trashed"] = "trashed"
    defaults["date"] = "date"
    defaults["new_date"] = "new_date"
    defaults.update(**kwargs)
    if "district" not in defaults:
        defaults["district"] = create_district()
    return DistrictExceptions.objects.create(**defaults)


def create_addressblock(**kwargs):
    defaults = {}
    defaults["address_range"] = "100-800"
    defaults["street"] = "Hammond St"
    defaults.update(**kwargs)
    if "district" not in defaults:
        defaults["district"] = create_district()
    return AddressBlock.objects.get_or_create(**defaults)[0]


def create_subscription(**kwargs):
    defaults = {}
    defaults["updated"] = "updated"
    defaults["trashed"] = "trashed"
    defaults["subscription_type"] = "subscription_type"
    defaults["district_id"] = create_district().id
    defaults.update(**kwargs)
    if "user" not in defaults:
        defaults["user"] = create_user()
    return Subscription.objects.create(**defaults)


class MunicipalityViewTest(unittest.TestCase):
    '''
    Tests for Municipality
    '''
    def setUp(self):
        self.client = Client()

    def test_list_municipality(self):
        url = reverse('notifications:municipality_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_municipality(self):
        url = reverse('notifications:municipality_create')
        data = {
            "slug": "bangor",
            "name": "Bangor",
            "state": "ME",
            "population": 30000,
            "approved": "approved",
            "contacts": create_user().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    '''
    def test_detail_municipality(self):
        municipality = create_municipality()
        url = reverse('notifications:municipality_detail', args=[municipality.slug,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    '''

    def test_update_municipality(self):
        municipality = create_municipality()
        data = {
            "slug": "slug",
            "name": "name",
            "updated": "updated",
            "trashed": "trashed",
            "state": "state",
            "population": "population",
            "approved": "approved",
            "contacts": create_user().id,
        }
        url = reverse('notifications:municipality_update', args=[municipality.slug,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 405)


#class DistrictViewTest(unittest.TestCase):
#    '''
#    Tests for District
#    '''
#    def setUp(self):
#        self.client = Client()
#
#    def test_list_district(self):
#        url = reverse('notifications:district_list')
#        response = self.client.get(url)
#        self.assertEqual(response.status_code, 200)
#
#    def test_create_district(self):
#        url = reverse('notifications:district_create')
#        data = {
#            "slug": "slug",
#            "name": "name",
#            "updated": "updated",
#            "trashed": "trashed",
#            "district_type": "district_type",
#            "pickup_time": "pickup_time",
#            "municipality": create_municipality().id,
#        }
#        response = self.client.post(url, data=data)
#        self.assertEqual(response.status_code, 302)
#
#    def test_detail_district(self):
#        district = create_district()
#        url = reverse('notifications:district_detail', args=[district.slug,])
#        response = self.client.get(url)
#        self.assertEqual(response.status_code, 200)
#
#    def test_update_district(self):
#        district = create_district()
#        data = {
#            "slug": "slug",
#            "name": "name",
#            "updated": "updated",
#            "trashed": "trashed",
#            "district_type": "district_type",
#            "pickup_time": "pickup_time",
#            "municipality": create_municipality().id,
#        }
#        url = reverse('notifications:district_update', args=[district.slug,])
#        response = self.client.post(url, data)
#        self.assertEqual(response.status_code, 302)


#class DistrictExceptionsViewTest(unittest.TestCase):
#    '''
#    Tests for DistrictExceptions
#    '''
#    def setUp(self):
#        self.client = Client()
#
#    def test_list_districtexceptions(self):
#        url = reverse('notifications:districtexceptions_list')
#        response = self.client.get(url)
#        self.assertEqual(response.status_code, 200)
#
#    def test_create_districtexceptions(self):
#        url = reverse('notifications:districtexceptions_create')
#        data = {
#            "slug": "slug",
#            "name": "name",
#            "updated": "updated",
#            "trashed": "trashed",
#            "date": "date",
#            "new_date": "new_date",
#            "district": create_district().id,
#        }
#        response = self.client.post(url, data=data)
#        self.assertEqual(response.status_code, 302)
#
#    def test_detail_districtexceptions(self):
#        districtexceptions = create_districtexceptions()
#        url = reverse('notifications:districtexceptions_detail', args=[districtexceptions.slug,])
#        response = self.client.get(url)
#        self.assertEqual(response.status_code, 200)
#
#    def test_update_districtexceptions(self):
#        districtexceptions = create_districtexceptions()
#        data = {
#            "slug": "slug",
#            "name": "name",
#            "updated": "updated",
#            "trashed": "trashed",
#            "date": "date",
#            "new_date": "new_date",
#            "district": create_district().id,
#        }
#        url = reverse('notifications:districtexceptions_update', args=[districtexceptions.slug,])
#        response = self.client.post(url, data)
#        self.assertEqual(response.status_code, 302)


#class AddressBlockViewTest(unittest.TestCase):
#    '''
#    Tests for AddressBlock
#    '''
#    def setUp(self):
#        self.client = Client()
#
#    def test_list_addressblock(self):
#        url = reverse('notifications:addressblock_list')
#        response = self.client.get(url)
#        self.assertEqual(response.status_code, 200)
#
#
#    def test_create_addressblock(self):
#        url = reverse('notifications:addressblock_create')
#        data = {
#            "address_range": "100-800",
#            "street": "Hammond St",
#            "district": create_district().id,
#        }
#        response = self.client.post(url, data=data)
#        self.assertEqual(response.status_code, 302)
#
#    def test_detail_addressblock(self):
#        addressblock = create_addressblock()
#        url = reverse('notifications:addressblock_detail', args=[addressblock.id,])
#        response = self.client.get(url)
#        self.assertEqual(response.status_code, 200)
#
#    def test_update_addressblock(self):
#        addressblock = create_addressblock()
#        data = {
#            "address_range": "100-800",
#            "street": "Hammond St",
#            "district": create_district().id,
#        }
#        url = reverse('notifications:addressblock_update', args=[addressblock.id,])
#        response = self.client.post(url, data)
#        self.assertEqual(response.status_code, 302)


class SubscriptionViewTest(unittest.TestCase):
    '''
    Tests for Subscription
    '''
    def setUp(self):
        self.client = Client()

    def test_list_subscription(self):
        url = reverse('notifications:subscription_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_create_subscription(self):
        url = reverse('notifications:subscription_create')
        data = {
            "slug": "slug",
            "name": "name",
            "updated": "updated",
            "trashed": "trashed",
            "subscription_type": "subscription_type",
            "user": create_user().id,
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 302)

    def test_detail_subscription(self):
        subscription = create_subscription()
        url = reverse('notifications:subscription_detail', args=[subscription.id,])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_update_subscription(self):
        subscription = create_subscription()
        data = {
            "updated": "updated",
            "trashed": "trashed",
            "subscription_type": "subscription_type",
            "user": create_user().id,
        }
        url = reverse('notifications:subscription_update', args=[subscription.id,])
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, 302)


