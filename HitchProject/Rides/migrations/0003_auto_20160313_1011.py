# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 10:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Rides', '0002_auto_20160313_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ride',
            name='departure',
        ),
        migrations.RemoveField(
            model_name='ride',
            name='destination',
        ),
    ]