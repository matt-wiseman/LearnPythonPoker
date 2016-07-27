# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2016-07-26 22:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poker_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='rank',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Ace'), (2, 'Two'), (3, 'Three'), (4, 'Four'), (5, 'Five'), (6, 'Six'), (7, 'Seven'), (8, 'Eight'), (9, 'Nine'), (10, 'Ten'), (11, 'Jack'), (12, 'Queen'), (13, 'King')]),
        ),
        migrations.AlterField(
            model_name='card',
            name='suit',
            field=models.PositiveSmallIntegerField(choices=[(0, 'Spades'), (1, 'Diamonds'), (2, 'Clubs'), (3, 'Hearts')]),
        ),
    ]
