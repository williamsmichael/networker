# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20151109_0127'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usereducation',
            old_name='education_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='usereducation',
            old_name='education_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='usereducation',
            old_name='school_year_ended',
            new_name='year_ended',
        ),
        migrations.RenameField(
            model_name='usereducation',
            old_name='school_year_started',
            new_name='year_started',
        ),
        migrations.RenameField(
            model_name='userjob',
            old_name='company_country',
            new_name='country',
        ),
        migrations.RenameField(
            model_name='userjob',
            old_name='job_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='userjob',
            old_name='company_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='userjob',
            old_name='company_state_province',
            new_name='state_province',
        ),
        migrations.RenameField(
            model_name='userjob',
            old_name='job_title',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='userjob',
            old_name='company_year_ended',
            new_name='year_ended',
        ),
        migrations.RenameField(
            model_name='userjob',
            old_name='company_year_started',
            new_name='year_started',
        ),
    ]
