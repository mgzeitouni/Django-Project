# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0004_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='first_visit',
            field=models.TimeField(default=datetime.datetime(2015, 12, 15, 15, 32, 51, 72974)),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='last_visit',
            field=models.TimeField(default=datetime.datetime(2015, 12, 15, 15, 32, 51, 72993)),
            preserve_default=True,
        ),
    ]
