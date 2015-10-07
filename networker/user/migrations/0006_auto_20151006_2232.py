# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20151006_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userphone',
            name='country_code',
            field=models.PositiveSmallIntegerField(null=True, blank=True),
        ),
    ]
