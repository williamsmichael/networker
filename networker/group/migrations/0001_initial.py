# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import group.models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NetworkerGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, serialize=False, primary_key=True)),
                ('name', models.CharField(blank=True, max_length=255)),
                ('description', models.TextField(blank=True)),
                ('welcome_message', models.TextField(blank=True)),
                ('profile_image', models.ImageField(blank=True, upload_to=group.models.upload_to, null=True)),
                ('website', models.URLField(blank=True)),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('forum', models.OneToOneField(to='forum.Forum')),
                ('organizer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
    ]
