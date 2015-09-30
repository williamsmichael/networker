# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('last_message_dateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageSystemMessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('message', models.TextField()),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('group_user_id', models.ForeignKey(to='group.GroupUser')),
            ],
        ),
        migrations.CreateModel(
            name='MessageSystemTopic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('topic_name', models.CharField(max_length=255)),
                ('topic_description', models.TextField()),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkerGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('group_name', models.CharField(max_length=255)),
                ('group_description', models.TextField(max_length=255, blank=True)),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('group_organizer', models.ForeignKey(to='user.NetworkerUser')),
            ],
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
            field=models.ForeignKey(to='user.NetworkerUser'),
        ),
    ]
