# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20150929_1920'),
    ]

    operations = [
        migrations.CreateModel(
            name='Networker_User',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('relationship_to_group', models.CharField(max_length=50)),
                ('other_email', models.CharField(unique=True, max_length=50)),
                ('date_of_birth', models.DateTimeField()),
                ('user_timezone', models.DateField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('last_login_dateTime', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.AlterField(
            model_name='user_address',
            name='latitude_api',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='longitude_api',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='user_address',
            name='user_id',
            field=models.ForeignKey(to='user.Networker_User'),
        ),
        migrations.AlterField(
            model_name='user_education',
            name='user_id',
            field=models.ForeignKey(to='user.Networker_User'),
        ),
        migrations.AlterField(
            model_name='user_email',
            name='user_id',
            field=models.ForeignKey(to='user.Networker_User'),
        ),
        migrations.AlterField(
            model_name='user_job',
            name='user_id',
            field=models.ForeignKey(to='user.Networker_User'),
        ),
        migrations.AlterField(
            model_name='user_phone',
            name='user_id',
            field=models.ForeignKey(to='user.Networker_User'),
        ),
        migrations.AlterField(
            model_name='user_skill',
            name='user_id',
            field=models.ForeignKey(to='user.Networker_User'),
        ),
        migrations.AlterField(
            model_name='user_social_media',
            name='user_id',
            field=models.ForeignKey(to='user.Networker_User'),
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
