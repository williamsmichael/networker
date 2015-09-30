# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
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
            name='NetworkerGroup',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('group_name', models.CharField(max_length=255)),
                ('group_description', models.TextField(max_length=255, blank=True)),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='group_user',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='group_user',
            name='user_id',
        ),
        migrations.RemoveField(
            model_name='message_system_message',
            name='group_user_id',
        ),
        migrations.RemoveField(
            model_name='message_system_message',
            name='message_system_topic_id',
        ),
        migrations.RemoveField(
            model_name='message_system_topic',
            name='group_id',
        ),
        migrations.RemoveField(
            model_name='message_system_topic',
            name='originator_id',
        ),
        migrations.RemoveField(
            model_name='networker_group',
            name='group_organizer',
        ),
        migrations.DeleteModel(
            name='Group_User',
        ),
        migrations.DeleteModel(
            name='Message_System_Message',
        ),
        migrations.DeleteModel(
            name='Message_System_Topic',
        ),
        migrations.DeleteModel(
            name='Networker_Group',
        ),
    ]
