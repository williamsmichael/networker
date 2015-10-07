# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20151006_2232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='networkeruser',
            options={'ordering': ['id']},
        ),
    ]
