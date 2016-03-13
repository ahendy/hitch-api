# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-12 23:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.DecimalField(decimal_places=6, max_digits=9)),
                ('longi', models.DecimalField(decimal_places=6, max_digits=9)),
                ('addr', models.CharField(max_length=70)),
                ('State_Prov', models.CharField(max_length=70)),
                ('zip_code', models.CharField(max_length=7)),
            ],
        ),
    ]