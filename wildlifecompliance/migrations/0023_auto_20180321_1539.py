# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-21 07:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wildlifecompliance', '0022_auto_20180321_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wildlifelicencecategory',
            name='activity',
            field=models.ManyToManyField(
                blank=True,
                to='wildlifecompliance.WildlifeLicenceActivityType'),
        ),
    ]
