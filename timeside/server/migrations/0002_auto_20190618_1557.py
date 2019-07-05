# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2019-06-18 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timeside_server', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processor',
            name='pid',
            field=models.CharField(max_length=128, verbose_name='pid'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='pid',
            field=models.CharField(blank=True, max_length=128, verbose_name='pid'),
        ),
    ]