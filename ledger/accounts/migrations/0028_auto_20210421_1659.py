# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-04-21 08:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20210421_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailuser',
            name='billing_same_as_residential',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='emailuser',
            name='postal_same_as_residential',
            field=models.BooleanField(default=False),
        ),
    ]
