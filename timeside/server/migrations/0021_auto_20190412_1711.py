# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2019-04-12 15:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('timeside_server', '0020_task_item'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provideridentifier',
            name='provider',
        ),
        migrations.RemoveField(
            model_name='item',
            name='code',
        ),
        migrations.RemoveField(
            model_name='item',
            name='external_id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='provider_identifier',
        ),
        migrations.RemoveField(
            model_name='provider',
            name='url',
        ),
        migrations.AddField(
            model_name='item',
            name='provider',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='timeside_server.Provider', verbose_name='provider'),
        ),
        migrations.AddField(
            model_name='provider',
            name='pid',
            field=models.CharField(blank=True, max_length=128, unique=True, verbose_name='pid'),
        ),
        migrations.DeleteModel(
            name='ProviderIdentifier',
        ),
    ]