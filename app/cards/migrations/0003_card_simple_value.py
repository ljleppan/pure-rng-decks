# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-08-02 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0002_auto_20160802_1410'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='simple_value',
            field=models.FloatField(default=0),
            preserve_default=False,
        ),
    ]