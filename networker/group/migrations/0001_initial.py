# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
        ('auth', '0006_require_contenttypes_0002'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_message_dateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageSystemMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField()),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('group_user_id', models.ForeignKey(to='group.GroupUser')),
            ],
        ),
        migrations.CreateModel(
            name='MessageSystemTopic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('topic_name', models.CharField(max_length=255)),
                ('topic_description', models.TextField()),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='MessageSystemTopicTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=25, blank=True)),
                ('message_system_topic_tag_id', models.ForeignKey(to='group.MessageSystemTopic')),
            ],
        ),
        migrations.CreateModel(
            name='NetworkerGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_description', models.TextField(max_length=255, blank=True)),
                ('welcome_message', models.TextField(max_length=255, blank=True)),
                ('group_image', models.ImageField(upload_to='static/images', blank=True)),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('group_extension', models.OneToOneField(to='auth.Group')),
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
