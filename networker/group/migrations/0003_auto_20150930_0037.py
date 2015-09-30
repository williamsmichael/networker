# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20150930_0037'),
        ('group', '0002_auto_20150930_0037'),
    ]

    operations = [
        migrations.AddField(
            model_name='networkergroup',
            name='group_organizer',
            field=models.ForeignKey(to='user.NetworkerUser'),
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
            name='group_user_id',
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
