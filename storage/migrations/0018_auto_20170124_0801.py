# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-24 08:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0017_auto_20170103_2209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='Equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='storage.Equipment'),
        ),
    ]