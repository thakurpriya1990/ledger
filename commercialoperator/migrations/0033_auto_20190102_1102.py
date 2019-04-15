# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-01-02 03:02
from __future__ import unicode_literals

import commercialoperator.components.compliances.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commercialoperator', '0032_auto_20190102_1100'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.CharField(blank=True, max_length=200)),
                ('rego', models.CharField(blank=True, max_length=200)),
                ('license', models.CharField(blank=True, max_length=200)),
                ('rego_expiry', models.DateField(blank=True, null=True)),
                ('access_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='vehicles', to='commercialoperator.AccessType')),
            ],
        ),
        migrations.AlterField(
            model_name='compliancedocument',
            name='_file',
            field=models.FileField(upload_to=commercialoperator.components.compliances.models.update_proposal_complaince_filename),
        ),
    ]