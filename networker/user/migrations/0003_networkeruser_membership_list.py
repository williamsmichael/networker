# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0003_remove_groupuser_user_id'),
        ('user', '0002_auto_20151026_0138'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkeruser',
            name='membership_list',
            field=models.ManyToManyField(to='group.NetworkerGroup'),
        ),
    ]
