# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 22:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker_api', '0007_auto_20160726_2245'),
    ]

    operations = [
        migrations.AlterField(
            model_name='table',
            name='pot',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
