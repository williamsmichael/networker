# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_auto_20151006_2232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='networkergroup',
            options={'ordering': ['id']},
        ),
    ]
