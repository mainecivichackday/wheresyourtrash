from __future__ import unicode_literals

import uuid
from datetime import datetime
from django.db import models
from django.utils.translation import ugettext as _
from django.template.defaultfilters import slugify
from localflavor.us.models import USStateField, USZipCodeField
from custom_user.models import EmailUser as User
from recurrent import RecurringEvent
from dateutil import rrule

from .managers import TrashManager

DISTRICT_TYPES = (
    ('TRASH', 'Trash'),
    ('RECYCLING', 'Recycling'),
)

SUB_TYPES = (
    #('SMS', 'Text message'),
    ('EMAIL', 'Email'),
)


class BaseMixin(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    slug = models.SlugField(blank=True, null=True)
    name = models.CharField(_("Name"), max_length=255)
    created = models.DateTimeField(_("Created"), auto_now=True, db_index=True)
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

    def __unicode__(self):
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
    state = USStateField()
    population = models.IntegerField(_("Population"), null=True, blank=True)
    contacts = models.ManyToManyField(User)
    approved = models.BooleanField(_("Approved"), default=True)
    zipcode =  USZipCodeField()

    def __unicode__(self):
        return u'{0}, {1}'.format(self.name, self.state)


class District(TrashableMixin):
    municipality = models.ForeignKey(Municipality)
    district_type = models.CharField(_("District type"), max_length=50,
                                     choices=DISTRICT_TYPES)
    identifier = models.CharField(_("Identifier"), blank=True, null=True, max_length=255)
    pickup_time = models.CharField(_("Pick up time"), max_length=255)

    def __unicode__(self):
        return u'{0} district for {1}'.format(self.get_district_type_display(),
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

class DistrictExceptions(BaseMixin):
    district = models.ForeignKey(District)
    date = models.DateField(_("Date"))
    new_date = models.DateField(_("New date"), blank=True, null=True)

    @property
    def cancelled(self):
        cancelled = False
        if not self.new_date:
            cancelled = True
        return cancelled


class AddressBlock(models.Model):
    district = models.ForeignKey(District)
    address_range = models.CharField(_("Address range"), max_length=255)
    street = models.CharField(_("Street"), max_length=255)


class Subscription(TrashableMixin):
    user = models.ForeignKey(User)
    subscription_type = models.CharField(_("Type"), choices=SUB_TYPES,
                                         max_length=20)
    district = models.ForeignKey(District)

