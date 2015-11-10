# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import group.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkerGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=255, blank=True)),
                ('description', models.TextField(blank=True)),
                ('welcome_message', models.TextField(blank=True)),
                ('profile_image', models.ImageField(null=True, upload_to=group.models.upload_to, blank=True)),
                ('website', models.URLField(blank=True)),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('organizer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
