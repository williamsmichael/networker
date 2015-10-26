# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraddress',
            old_name='deactivate',
            new_name='remove',
        ),
        migrations.RenameField(
            model_name='usereducation',
            old_name='deactivate',
            new_name='remove',
        ),
        migrations.RenameField(
            model_name='useremail',
            old_name='deactivate',
            new_name='remove',
        ),
        migrations.RenameField(
            model_name='userjob',
            old_name='deactivate',
            new_name='remove',
        ),
        migrations.RenameField(
            model_name='userphone',
            old_name='deactivate',
            new_name='remove',
        ),
        migrations.RenameField(
            model_name='userskill',
            old_name='deactivate',
            new_name='remove',
        ),
        migrations.RenameField(
            model_name='usersocialmedia',
            old_name='deactivate',
            new_name='remove',
        ),
    ]
