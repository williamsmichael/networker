# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_remove_networkergroup_forum'),
        ('forum', '0002_forum_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='group',
            field=models.ForeignKey(default=1, to='group.NetworkerGroup'),
            preserve_default=False,
        ),
    ]
