# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-06-18 07:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('disturbance', '0005_auto_20180618_1123'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposalapprovergroup',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='proposalapprovergroup',
            name='regions',
        ),
        migrations.RemoveField(
            model_name='proposalassessorgroup',
            name='activities',
        ),
        migrations.RemoveField(
            model_name='proposalassessorgroup',
            name='regions',
        ),
    ]