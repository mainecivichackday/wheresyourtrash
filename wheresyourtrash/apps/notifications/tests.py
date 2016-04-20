import mock
import unittest
from django.test import TestCase

from datetime import datetime, timedelta

from notifications.models import District, DistrictExceptions, Municipality

class DistrictTestCase(TestCase):
    def setUp(self):
        today = datetime.now()
        m = Municipality.objects.create(state="ME", zipcode="04421",
                                    name="Castine")
        District.objects.create(municipality=m,
                                pickup_time="every monday",
                                district_type="TRASH")

    def test_next_pickup_date_correct(self):
        """District property should return next date correctly"""
        district = District.objects.get(district_type="TRASH")
        today = datetime.now()
        next_monday = today + timedelta(days=-today.weekday(), weeks=1)
        self.assertEqual(district.next_pickup, next_monday.date())

        DistrictExceptions.objects.create(district=district,
                                          date=next_monday) 
        next_next_monday = next_monday + timedelta(days=-next_monday.weekday(),
                                                   weeks=1)
        self.assertEqual(district.next_pickup, next_next_monday.date())
