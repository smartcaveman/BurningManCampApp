# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-07-31 18:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0010_add_user_notes_and_not_null_length'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='width',
            field=models.FloatField(choices=[(3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0), (8.5, 8.5), (9.0, 9.0), (9.5, 9.5), (10.0, 10.0), (10.5, 10.5), (11.0, 11.0), (11.5, 11.5), (12.0, 12.0), (12.5, 12.5), (13.0, 13.0), (13.5, 13.5), (14.0, 14.0), (14.5, 14.5), (15.0, 15.0), (15.5, 15.5), (16.0, 16.0), (16.5, 16.5), (17.0, 17.0), (17.5, 17.5), (18.0, 18.0), (18.5, 18.5), (19.0, 19.0), (19.5, 19.5)], default=3),
            preserve_default=False,
        ),
    ]