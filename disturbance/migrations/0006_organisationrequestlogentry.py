# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-06-09 00:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0005_merge_20170608_1301'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrganisationRequestLogEntry',
            fields=[
                ('communicationslogentry_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='disturbance.CommunicationsLogEntry')),
                ('request', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='disturbance.OrganisationRequest')),
            ],
            bases=('disturbance.communicationslogentry',),
        ),
    ]