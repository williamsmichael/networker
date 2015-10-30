# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import group.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('last_message_dateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageSystemMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('message', models.TextField()),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('group_user_id', models.ForeignKey(to='group.GroupUser')),
            ],
        ),
        migrations.CreateModel(
            name='MessageSystemTopic',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('topic_name', models.CharField(max_length=255)),
                ('topic_description', models.TextField()),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageSystemTopicTag',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('tag', models.CharField(max_length=255, blank=True)),
                ('message_system_topic_tag_id', models.ForeignKey(to='group.MessageSystemTopic')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkerGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
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
        migrations.AddField(
            model_name='messagesystemtopic',
            name='group_id',
            field=models.ForeignKey(to='group.NetworkerGroup'),
        ),
        migrations.AddField(
            model_name='messagesystemtopic',
            name='originator_id',
            field=models.ForeignKey(to='group.GroupUser'),
        ),
        migrations.AddField(
            model_name='messagesystemmessage',
            name='message_system_topic_id',
            field=models.ForeignKey(to='group.MessageSystemTopic'),
        ),
        migrations.AddField(
            model_name='groupuser',
            name='group_id',
            field=models.ForeignKey(to='group.NetworkerGroup'),
        ),
        migrations.AddField(
            model_name='groupuser',
            name='user_id',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
