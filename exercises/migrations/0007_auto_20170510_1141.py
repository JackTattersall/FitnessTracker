# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 11:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0006_auto_20170509_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='workout',
            name='name',
            field=models.CharField(default='workout 10-5-2017-11h0001-01-01 00:00:00m27s', max_length=255),
        ),
    ]
