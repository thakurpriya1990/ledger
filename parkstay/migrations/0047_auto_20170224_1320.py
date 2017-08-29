# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-24 05:20
from __future__ import unicode_literals
import traceback
from django.db import migrations, models
import django.db.models.deletion

def create_booking_invoice_records(apps, schema_editor):
    Booking = apps.get_model('parkstay','Booking')
    BookingInvoice = apps.get_model('parkstay','BookingInvoice')
    try:
        for b in Booking.objects.all():
            if b.invoice_reference:
                BookingInvoice.objects.create(booking=b,invoice_reference=b.invoice_reference)
    except Exception as e:
        traceback.print_exc()
        raise e

class Migration(migrations.Migration):

    dependencies = [
        ('parkstay', '0046_auto_20170224_0915'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingInvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_reference', models.CharField(blank=True, default='', max_length=50, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='bookinginvoice',
            name='booking',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='parkstay.Booking'),
        ),
        migrations.RunPython(create_booking_invoice_records),
        migrations.RemoveField(
            model_name='booking',
            name='invoice_reference',
        ),
    ]