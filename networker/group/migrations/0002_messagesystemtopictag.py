# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MessageSystemTopicTag',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='ID', auto_created=True)),
                ('tag', models.CharField(max_length=25, blank=True)),
                ('message_system_topic_tag_id', models.ForeignKey(to='group.MessageSystemTopic')),
            ],
        ),
    ]
