# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20151109_0148'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userjob',
            old_name='name',
            new_name='company_name',
        ),
    ]
