# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-10 15:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='address',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='location',
            name='hours',
            field=models.TextField(blank=True, null=True),
        ),
    ]
