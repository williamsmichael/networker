# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_messagesystemtopictag'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkergroup',
            name='group_image',
            field=models.ImageField(upload_to='static/images', default=datetime.datetime(2015, 10, 2, 16, 58, 23, 388482, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='networkergroup',
            name='welcome_message',
            field=models.TextField(max_length=255, blank=True),
        ),
    ]
