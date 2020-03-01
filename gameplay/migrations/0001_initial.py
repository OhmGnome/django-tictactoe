# -*- coding: utf-8 -*-
# Generated by Django 1.11b1 on 2017-05-01 11:32
# from .../models.py
# Migration helps keep local dev and environment databases in sync (like java hibernate)
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(auto_now_add=True)),
                ('last_active', models.DateTimeField(auto_now=True)),
                ('first_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_first_player', to=settings.AUTH_USER_MODEL)),
                ('second_player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='games_second_player', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Move',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('x', models.IntegerField()),
                ('y', models.IntegerField()),
                ('comment', models.CharField(max_length=300)),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gameplay.Game')),
            ],
        ),
    ]
