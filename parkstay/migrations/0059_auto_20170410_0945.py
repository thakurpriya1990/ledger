# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-10 01:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0058_campsiteclass_max_vehicles'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campground',
            name='customer_contact',
        ),
        migrations.AddField(
            model_name='contact',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default='visitor.services@dpaw.wa.gov.au', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='opening_hours',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='other_services',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone_number',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.DeleteModel(
            name='CustomerContact',
        ),
    ]
