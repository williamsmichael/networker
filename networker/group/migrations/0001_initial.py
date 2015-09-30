# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20150929_2219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group_User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('last_message_dateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message_System_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('message', models.TextField()),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('group_user_id', models.ForeignKey(to='group.Group_User')),
            ],
        ),
        migrations.CreateModel(
            name='Message_System_Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('topic_name', models.CharField(max_length=255)),
                ('topic_description', models.TextField()),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Networker_Group',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('group_name', models.CharField(max_length=255)),
                ('group_description', models.TextField(blank=True, max_length=255)),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('group_organizer', models.ForeignKey(to='user.Networker_User')),
            ],
        ),
        migrations.AddField(
            model_name='message_system_topic',
            name='group_id',
            field=models.ForeignKey(to='group.Networker_Group'),
        ),
        migrations.AddField(
            model_name='message_system_topic',
            name='originator_id',
            field=models.ForeignKey(to='group.Group_User'),
        ),
        migrations.AddField(
            model_name='message_system_message',
            name='message_system_topic_id',
            field=models.ForeignKey(to='group.Message_System_Topic'),
        ),
        migrations.AddField(
            model_name='group_user',
            name='group_id',
            field=models.ForeignKey(to='group.Networker_Group'),
        ),
        migrations.AddField(
            model_name='group_user',
            name='user_id',
            field=models.ForeignKey(to='user.Networker_User'),
        ),
    ]
