# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-10 18:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0007_auto_20170510_1141'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workout',
            name='name',
        ),
    ]