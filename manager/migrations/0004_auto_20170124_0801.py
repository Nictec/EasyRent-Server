# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-24 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0003_auto_20170109_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipment',
            name='Image',
            field=models.ImageField(null=True, upload_to='media'),
        ),
        migrations.AddField(
            model_name='equipment',
            name='beschreibung',
            field=models.CharField(default='-', max_length=200),
            preserve_default=False,
        ),
    ]
