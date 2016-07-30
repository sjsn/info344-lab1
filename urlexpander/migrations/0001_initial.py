# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-29 21:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='URL',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=250)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
