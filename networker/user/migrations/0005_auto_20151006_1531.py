# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import user.models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20151006_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkeruser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=user.models.upload_to),
        ),
    ]
