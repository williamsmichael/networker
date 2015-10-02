# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0004_networkergroup_group_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='networkergroup',
            name='group_extension',
            field=models.ManyToManyField(to='auth.Group'),
        ),
    ]
