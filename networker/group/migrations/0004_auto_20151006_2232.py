# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import group.models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_auto_20151006_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkergroup',
            name='group_image',
            field=models.ImageField(null=True, upload_to=group.models.upload_to, blank=True),
        ),
    ]
