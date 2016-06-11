# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-11 16:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_auto_20160419_2148'),
    ]

    operations = [
        migrations.AddField(
            model_name='addressblock',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, default=datetime.datetime(2016, 6, 11, 16, 33, 16, 207636, tzinfo=utc), verbose_name='Created'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addressblock',
            name='name',
            field=models.CharField(default='', max_length=255, verbose_name='Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addressblock',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='addressblock',
            name='trashed',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AddField(
            model_name='addressblock',
            name='updated',
            field=models.DateTimeField(auto_now=True, db_index=True, default=datetime.datetime(2016, 6, 11, 16, 33, 33, 623549, tzinfo=utc), verbose_name='Updated'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='districtexceptions',
            name='trashed',
            field=models.BooleanField(db_index=True, default=False),
        ),
        migrations.AlterField(
            model_name='addressblock',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='district',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='districtexceptions',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='municipality',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created'),
        ),
        migrations.AlterField(
            model_name='subscription',
            name='created',
            field=models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Created'),
        ),
    ]
