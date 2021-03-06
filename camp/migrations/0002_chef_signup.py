# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-22 00:54
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('camp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500, unique=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
            ],
            options={
                'ordering': ('start_date',)
            }
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.DateField()),
                ('kind', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Dinner', 'Dinner')], default='Dinner', max_length=10)),
                ('private_notes', models.TextField(blank=True, help_text='Private to you')),
                ('public_notes', models.TextField(blank=True, help_text='Public description')),
                ('chef', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(help_text='What year/regional is this for?', on_delete=django.db.models.deletion.CASCADE, to='camp.Event')),
            ],
            options={
                'ordering': ('day', 'kind'),
            },
        ),
        migrations.AlterModelOptions(
            name='mealshift',
            options={'ordering': ('meal', 'role', 'pk')},
        ),
        migrations.RenameField(
            model_name='bikemutationschedule',
            old_name='camper',
            new_name='worker',
        ),
        migrations.AddField(
            model_name='mealshift',
            name='role',
            field=models.CharField(choices=[('courier', 'Courier'), ('chef', 'Chef'), ('sous-chef', 'Sous Chef'), ('kp', 'KP (cleaning/assistance)')], default='kp', max_length=10),
        ),
        migrations.AddField(
            model_name='mealshift',
            name='worker',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mealshift',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shifts', to='camp.Meal'),
        ),
        migrations.AlterUniqueTogether(
            name='mealshift',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='mealshift',
            name='assigned',
        ),
        migrations.RemoveField(
            model_name='mealshift',
            name='camper',
        ),
        migrations.RemoveField(
            model_name='mealshift',
            name='date',
        ),
        migrations.RemoveField(
            model_name='mealshift',
            name='day',
        ),
        migrations.RemoveField(
            model_name='mealshift',
            name='shift',
        ),
    ]
