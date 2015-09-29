# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='last_login_dateTime',
            field=models.DateTimeField(default=datetime.datetime(2015, 9, 29, 19, 20, 44, 925445)),
        ),
    ]
