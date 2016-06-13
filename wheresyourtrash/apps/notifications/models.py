from __future__ import unicode_literals

import uuid
from datetime import datetime, timedelta
from django.db import models
from django.utils.translation import ugettext as _
from localflavor.us.models import USStateField, USZipCodeField, PhoneNumberField
from custom_user.models import EmailUser as User
from dateutil import rrule
from django.core.urlresolvers import reverse
from django_extensions.db import fields as extension_fields

from recurrent import RecurringEvent
from email2sms.models import Provider

from .managers import TrashManager

DISTRICT_TYPES = (
    ('TRASH', 'Trash'),
    ('RECYCLING', 'Recycling'),
)

SUB_TYPES = (
    ('SMS', 'Text message'),
    ('EMAIL', 'Email'),
)


class BaseMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255)
    created = models.DateTimeField(_("Created"), auto_now_add=True, db_index=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True, db_index=True)

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(BaseMixin, self).__init__(*args, **kwargs)

    # Override save method.
    def save(self,  *args, **kwargs):
        update = kwargs.pop('update', False)
        if update:
            self.updated= datetime.now()

        super(BaseMixin, self).save(*args, **kwargs)

    def __str__(self):
        return u'{0}'.format(self.name)

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name, self.state)
        super(BaseMixin, self).save(*args, **kwargs)


class TrashableMixin(BaseMixin):
    trashed = models.BooleanField(default=False, db_index=True)

    objects = TrashManager()

    class Meta:
        abstract = True

    def __init__(self, *args, **kwargs):
        super(TrashableMixin, self).__init__(*args, **kwargs)

    # Override delete method.
    def delete(self, **kwargs):
        self._forced_delete = kwargs.pop('forced', False)
        if not self._forced_delete:
            model = self.__class__
            kwargs.update({'trashed': True})
            model.objects.using(self._db).filter(
                    pk=self.id).update(**kwargs)
        else:
            super(TrashableMixin, self).delete(**kwargs)


class Municipality(TrashableMixin):
    districts_map = models.ImageField(_("Districts Map"), upload_to="notifications/maps/", blank=True, null=True)
    state = USStateField()
    population = models.IntegerField(_("Population"), null=True, blank=True)
    contacts = models.ManyToManyField(User)
    approved = models.BooleanField(_("Approved"), default=True)
    zipcode =  USZipCodeField()

    def __str__(self):
        return u'{0}, {1}'.format(self.name, self.state)

    def get_absolute_url(self):
        return reverse('notifications:municipality_detail', args=[str(self.slug)])

class District(TrashableMixin):
    municipality = models.ForeignKey(Municipality)
    district_type = models.CharField(_("District type"), max_length=50,
                                     choices=DISTRICT_TYPES)
    identifier = models.CharField(_("Identifier"), blank=True, null=True, max_length=255)
    pickup_time = models.CharField(_("Pick up time"), max_length=255)

    def __str__(self):
        return u'{0} {1} district for {2}'.format(self.name, self.get_district_type_display(),
                                              self.municipality)


    @property
    def next_pickup(self):
        r = RecurringEvent(now_date=datetime.now())
        r.parse(self.pickup_time)
        rr = rrule.rrulestr(r.get_RFC_rrule())
        next_date = rr.after(datetime.now())
        try:
            date_exception = DistrictExceptions.objects.get(date=next_date,
                                                            district=self)
        except:
            date_exception = None
        if date_exception:
            new_date = date_exception.new_date
            if not new_date:
                next_date = rr.after(next_date)
            else:
                next_date = new_date
        return next_date.date()

class DistrictExceptions(TrashableMixin):
    district = models.ForeignKey(District)
    date = models.DateField(_("Date"))
    new_date = models.DateField(_("New date"), blank=True, null=True)

    def __str__(self):
        return u'{0}'.format(self.name)

    @property
    def cancelled(self):
        cancelled = False
        if not self.new_date:
            cancelled = True
        return cancelled


class AddressBlock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True, db_index=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True, db_index=True)
    district = models.ForeignKey(District)
    address_range = models.CharField(_("Address range"), max_length=255)
    street = models.CharField(_("Street"), max_length=255)

    def __str__(self):
        return u'{0} - {1} {2}'.format(self.district, self.address_range, self.street)

class Subscription(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(_("Created"), auto_now_add=True, db_index=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True, db_index=True)
    trashed = models.BooleanField(default=False, db_index=True)
    user = models.ForeignKey(User)
    subscription_type = models.CharField(_("Type"), choices=SUB_TYPES,
                                         max_length=20)
    service_provider = models.ForeignKey(Provider, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    district = models.ForeignKey(District)
    suspended = models.BooleanField(default=False)

    @property
    def clean_phone_number(self):
        return self.phone_number.replace(' ','').replace('-','')

    @property
    def day_before_pickup(self):
        '''Boolean return as to whether a notification should go'''
        today = datetime.today().date()
        if self.district.next_pickup - today == timedelta(1):
            return True
        else:
            return False

    @property
    def day_of_pickup(self):
        '''Boolean return as to whether a notification should go'''
        today = datetime.today().date()
        if self.district.next_pickup - today == timedelta(7):
            return True
        else:
            return False


    def __str__(self):
        return u'{0} notifications for {1}'.format(self.subscription_type,
                                                          self.district)

    def get_absolute_url(self):
        return reverse('notifications:subscription_detail', args=[self.id])

    def delete(self, **kwargs):
        self._forced_delete = kwargs.pop('forced', False)
        if not self._forced_delete:
            model = self.__class__
            kwargs.update({'trashed': True})
            model.objects.using(self._db).filter(
                    pk=self.id).update(**kwargs)
        else:
            super(Subscription, self).delete(**kwargs)

