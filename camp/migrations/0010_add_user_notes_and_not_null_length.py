# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-31 18:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0009_null_vehicle'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='public_notes',
            field=models.TextField(blank=True, help_text="Tell us stuff that doesn't fit elsewhere."),
        ),
        migrations.AlterField(
            model_name='user',
            name='meal_restrictions',
            field=models.ManyToManyField(blank=True, related_name='campers', to='camp.MealRestriction'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='length',
            field=models.FloatField(choices=[(3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0), (8.5, 8.5), (9.0, 9.0), (9.5, 9.5), (10.0, 10.0), (10.5, 10.5), (11.0, 11.0), (11.5, 11.5), (12.0, 12.0), (12.5, 12.5), (13.0, 13.0), (13.5, 13.5), (14.0, 14.0), (14.5, 14.5), (15.0, 15.0), (15.5, 15.5), (16.0, 16.0), (16.5, 16.5), (17.0, 17.0), (17.5, 17.5), (18.0, 18.0), (18.5, 18.5), (19.0, 19.0), (19.5, 19.5)], default=3),
            preserve_default=False,
        ),
    ]
