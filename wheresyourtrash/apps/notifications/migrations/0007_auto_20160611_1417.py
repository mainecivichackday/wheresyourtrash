# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 18:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import localflavor.us.models


class Migration(migrations.Migration):

    dependencies = [
        ('email2sms', '0002_load_initial_data'),
        ('notifications', '0006_municipality_districts_map'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='phone_number',
            field=localflavor.us.models.PhoneNumberField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='subscription',
            name='service_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='email2sms.Provider'),
        ),
        migrations.AddField(
            model_name='subscription',
            name='suspended',
            field=models.BooleanField(default=False),
        ),
    ]
