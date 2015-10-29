# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('group', '0003_remove_groupuser_user_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='networkergroup',
            old_name='group_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='networkergroup',
            old_name='group_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='networkergroup',
            old_name='group_image',
            new_name='profile_image',
        ),
        migrations.AddField(
            model_name='networkergroup',
            name='organizer',
            field=models.ForeignKey(default=1, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
