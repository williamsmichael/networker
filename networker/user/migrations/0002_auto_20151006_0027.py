# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkeruser',
            name='nickname',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='networkeruser',
            name='place_of_birth',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='networkeruser',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='static/images'),
        ),
    ]
