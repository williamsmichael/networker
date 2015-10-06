# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkeruser',
            name='website',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='userphone',
            name='country_code',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
