# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-12-27 18:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0008_auto_20161210_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='Equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='storage.Equipment'),
        ),
    ]
