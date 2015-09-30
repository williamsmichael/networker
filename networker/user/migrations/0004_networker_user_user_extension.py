# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('user', '0003_auto_20150929_2219'),
    ]

    operations = [
        migrations.AddField(
            model_name='networker_user',
            name='user_extension',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=2),
            preserve_default=False,
        ),
    ]
