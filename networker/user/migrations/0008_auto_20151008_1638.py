# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0007_auto_20151007_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkeruser',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
    ]
