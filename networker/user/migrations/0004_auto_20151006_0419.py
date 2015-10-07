# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20151006_0415'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usereducation',
            name='education_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='job_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='userskill',
            name='skill_description',
            field=models.TextField(blank=True),
        ),
    ]