# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2017-06-05 01:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('report', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='summaries',
            new_name='summarie',
        ),
        migrations.AlterField(
            model_name='summary',
            name='create_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 6, 5, 9, 47, 12, 527000)),
        ),
    ]
