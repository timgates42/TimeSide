# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2016-12-14 15:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('timeside_server', '0014_analysis_parameters_schema'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='analysis',
            options={'verbose_name': 'Analysis', 'verbose_name_plural': 'Analyses'},
        ),
    ]
