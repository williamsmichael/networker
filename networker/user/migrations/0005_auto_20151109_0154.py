# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20151109_0149'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userskill',
            old_name='skill_description',
            new_name='description',
        ),
    ]
