# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_auto_20151008_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkeruser',
            name='relationship_to_group',
            field=models.CharField(max_length=255, blank=True),
        ),
    ]
