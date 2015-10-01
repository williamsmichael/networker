# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='networkeruser',
            name='created_dateTime',
        ),
        migrations.RemoveField(
            model_name='networkeruser',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='networkeruser',
            name='is_admin',
        ),
        migrations.RemoveField(
            model_name='networkeruser',
            name='last_login_dateTime',
        ),
        migrations.RemoveField(
            model_name='networkeruser',
            name='other_email',
        ),
        migrations.RemoveField(
            model_name='networkeruser',
            name='user_timezone',
        ),
        migrations.AlterField(
            model_name='networkeruser',
            name='profile_image',
            field=models.ImageField(upload_to='static/images'),
        ),
    ]
