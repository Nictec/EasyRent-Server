# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-03 22:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0015_auto_20170103_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='Equipment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order', to='storage.Equipment'),
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[(b'ok', b'bereit'), (b'notOK', b'nicht bereit')], default='glyphicon glyphicon-remove', max_length=30),
        ),
    ]
