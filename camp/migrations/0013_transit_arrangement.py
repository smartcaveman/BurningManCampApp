# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-31 20:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0012_auto_20160731_1925'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicle',
            name='primary_driver_in_your_party',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='transit_arrangement',
            field=models.IntegerField(choices=[(0, 'Not sure yet'), (1, 'Primary driver'), (2, 'Riding with someone else'), (3, 'Some other transit')], default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vehicle',
            name='transit_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provided_transit', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='shelter_provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='provided_shelter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='make_of_car',
            field=models.CharField(blank=True, default='', max_length=15),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='model_of_car',
            field=models.CharField(blank=True, default='', max_length=25),
        ),
    ]
