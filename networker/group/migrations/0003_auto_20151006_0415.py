# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0002_networkergroup_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='messagesystemtopictag',
            name='tag',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='networkergroup',
            name='group_description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='networkergroup',
            name='group_image',
            field=models.ImageField(max_length=255, upload_to='static/images', blank=True),
        ),
        migrations.AlterField(
            model_name='networkergroup',
            name='welcome_message',
            field=models.TextField(blank=True),
        ),
    ]
