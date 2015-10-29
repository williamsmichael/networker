# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkergroup',
            name='group_extension',
        ),
        migrations.RemoveField(
            model_name='networkergroup',
            name='group_organizer',
        ),
        migrations.AddField(
            model_name='networkergroup',
            name='group_name',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
