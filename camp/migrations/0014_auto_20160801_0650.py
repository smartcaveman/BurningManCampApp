# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-08-01 06:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('camp', '0013_transit_arrangement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shelter',
            name='length',
            field=models.FloatField(choices=[(3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0), (8.5, 8.5), (9.0, 9.0), (9.5, 9.5), (10.0, 10.0), (10.5, 10.5), (11.0, 11.0), (11.5, 11.5), (12.0, 12.0), (12.5, 12.5), (13.0, 13.0), (13.5, 13.5), (14.0, 14.0), (14.5, 14.5), (15.0, 15.0), (15.5, 15.5), (16.0, 16.0), (16.5, 16.5), (17.0, 17.0), (17.5, 17.5), (18.0, 18.0), (18.5, 18.5), (19.0, 19.0), (19.5, 19.5)], null=True),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='number_of_people_tent_sleeps',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='shelter',
            name='width',
            field=models.FloatField(choices=[(3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0), (8.5, 8.5), (9.0, 9.0), (9.5, 9.5), (10.0, 10.0), (10.5, 10.5), (11.0, 11.0), (11.5, 11.5), (12.0, 12.0), (12.5, 12.5), (13.0, 13.0), (13.5, 13.5), (14.0, 14.0), (14.5, 14.5), (15.0, 15.0), (15.5, 15.5), (16.0, 16.0), (16.5, 16.5), (17.0, 17.0), (17.5, 17.5), (18.0, 18.0), (18.5, 18.5), (19.0, 19.0), (19.5, 19.5)], null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='length',
            field=models.FloatField(blank=True, choices=[(3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0), (8.5, 8.5), (9.0, 9.0), (9.5, 9.5), (10.0, 10.0), (10.5, 10.5), (11.0, 11.0), (11.5, 11.5), (12.0, 12.0), (12.5, 12.5), (13.0, 13.0), (13.5, 13.5), (14.0, 14.0), (14.5, 14.5), (15.0, 15.0), (15.5, 15.5), (16.0, 16.0), (16.5, 16.5), (17.0, 17.0), (17.5, 17.5), (18.0, 18.0), (18.5, 18.5), (19.0, 19.0), (19.5, 19.5), (20.0, 20.0), (20.5, 20.5), (21.0, 21.0), (21.5, 21.5), (22.0, 22.0), (22.5, 22.5), (23.0, 23.0), (23.5, 23.5), (24.0, 24.0), (24.5, 24.5), (25.0, 25.0), (25.5, 25.5), (26.0, 26.0), (26.5, 26.5), (27.0, 27.0), (27.5, 27.5), (28.0, 28.0), (28.5, 28.5), (29.0, 29.0), (29.5, 29.5), (30.0, 30.0), (30.5, 30.5), (31.0, 31.0), (31.5, 31.5), (32.0, 32.0), (32.5, 32.5), (33.0, 33.0), (33.5, 33.5), (34.0, 34.0), (34.5, 34.5), (35.0, 35.0), (35.5, 35.5), (36.0, 36.0), (36.5, 36.5), (37.0, 37.0), (37.5, 37.5), (38.0, 38.0), (38.5, 38.5), (39.0, 39.0), (39.5, 39.5), (40.0, 40.0), (40.5, 40.5), (41.0, 41.0), (41.5, 41.5), (42.0, 42.0), (42.5, 42.5), (43.0, 43.0), (43.5, 43.5), (44.0, 44.0), (44.5, 44.5), (45.0, 45.0), (45.5, 45.5), (46.0, 46.0), (46.5, 46.5), (47.0, 47.0), (47.5, 47.5), (48.0, 48.0), (48.5, 48.5), (49.0, 49.0), (49.5, 49.5), (50.0, 50.0), (50.5, 50.5), (51.0, 51.0), (51.5, 51.5), (52.0, 52.0), (52.5, 52.5), (53.0, 53.0), (53.5, 53.5), (54.0, 54.0), (54.5, 54.5), (55.0, 55.0), (55.5, 55.5), (56.0, 56.0), (56.5, 56.5), (57.0, 57.0), (57.5, 57.5), (58.0, 58.0), (58.5, 58.5), (59.0, 59.0), (59.5, 59.5), (60.0, 60.0), (60.5, 60.5), (61.0, 61.0), (61.5, 61.5), (62.0, 62.0), (62.5, 62.5), (63.0, 63.0), (63.5, 63.5), (64.0, 64.0), (64.5, 64.5), (65.0, 65.0), (65.5, 65.5), (66.0, 66.0), (66.5, 66.5), (67.0, 67.0), (67.5, 67.5), (68.0, 68.0), (68.5, 68.5), (69.0, 69.0), (69.5, 69.5), (70.0, 70.0), (70.5, 70.5), (71.0, 71.0), (71.5, 71.5), (72.0, 72.0), (72.5, 72.5), (73.0, 73.0), (73.5, 73.5), (74.0, 74.0), (74.5, 74.5), (75.0, 75.0), (75.5, 75.5), (76.0, 76.0), (76.5, 76.5), (77.0, 77.0), (77.5, 77.5), (78.0, 78.0), (78.5, 78.5), (79.0, 79.0), (79.5, 79.5), (80.0, 80.0), (80.5, 80.5), (81.0, 81.0), (81.5, 81.5), (82.0, 82.0), (82.5, 82.5), (83.0, 83.0), (83.5, 83.5), (84.0, 84.0), (84.5, 84.5), (85.0, 85.0), (85.5, 85.5), (86.0, 86.0), (86.5, 86.5), (87.0, 87.0), (87.5, 87.5), (88.0, 88.0), (88.5, 88.5), (89.0, 89.0), (89.5, 89.5), (90.0, 90.0), (90.5, 90.5), (91.0, 91.0), (91.5, 91.5), (92.0, 92.0), (92.5, 92.5), (93.0, 93.0), (93.5, 93.5), (94.0, 94.0), (94.5, 94.5), (95.0, 95.0), (95.5, 95.5), (96.0, 96.0), (96.5, 96.5), (97.0, 97.0), (97.5, 97.5), (98.0, 98.0), (98.5, 98.5)], null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='width',
            field=models.FloatField(blank=True, choices=[(3.0, 3.0), (3.5, 3.5), (4.0, 4.0), (4.5, 4.5), (5.0, 5.0), (5.5, 5.5), (6.0, 6.0), (6.5, 6.5), (7.0, 7.0), (7.5, 7.5), (8.0, 8.0), (8.5, 8.5), (9.0, 9.0), (9.5, 9.5), (10.0, 10.0), (10.5, 10.5), (11.0, 11.0), (11.5, 11.5), (12.0, 12.0), (12.5, 12.5), (13.0, 13.0), (13.5, 13.5), (14.0, 14.0), (14.5, 14.5), (15.0, 15.0), (15.5, 15.5), (16.0, 16.0), (16.5, 16.5), (17.0, 17.0), (17.5, 17.5), (18.0, 18.0), (18.5, 18.5), (19.0, 19.0), (19.5, 19.5)], null=True),
        ),
    ]