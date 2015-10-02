# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0003_auto_20151002_1658'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkergroup',
            name='group_extension',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
