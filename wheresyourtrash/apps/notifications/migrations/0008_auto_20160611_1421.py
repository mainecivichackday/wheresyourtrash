# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-11 18:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20160611_1417'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subscription',
            name='name',
        ),
        migrations.RemoveField(
            model_name='subscription',
            name='slug',
        ),
    ]
