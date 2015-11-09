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
            old_name='address_category_id',
            new_name='address_category',
        ),
        migrations.RenameField(
            model_name='usereducation',
            old_name='education_category_id',
            new_name='education_category',
        ),
        migrations.RenameField(
            model_name='useremail',
            old_name='email_category_id',
            new_name='email_category',
        ),
        migrations.RenameField(
            model_name='userjob',
            old_name='job_category_id',
            new_name='job_category',
        ),
        migrations.RenameField(
            model_name='userphone',
            old_name='phone_category_id',
            new_name='phone_category',
        ),
        migrations.RenameField(
            model_name='userskill',
            old_name='skill_category_id',
            new_name='skill_category',
        ),
        migrations.RenameField(
            model_name='usersocialmedia',
            old_name='social_media_category_id',
            new_name='social_media_category',
        ),
    ]
