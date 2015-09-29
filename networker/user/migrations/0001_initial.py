# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('address_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Education_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('education_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Email_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('email_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Job_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('job_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Phone_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('phone_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Skill_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('skill_category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Social_Media_Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('social_media_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('username', models.CharField(max_length=50)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('relationship_to_group', models.CharField(max_length=50)),
                ('primary_email', models.CharField(max_length=50, unique=True)),
                ('date_of_birth', models.DateTimeField()),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('last_login_dateTime', models.DateTimeField(default=datetime.datetime(2015, 9, 29, 18, 54, 26, 905446))),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='User_Address',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('street_address_1', models.CharField(max_length=50)),
                ('street_address_2', models.CharField(max_length=50)),
                ('city_town', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=25)),
                ('latitude_api', models.CharField(max_length=25)),
                ('longitude_api', models.CharField(max_length=25)),
                ('address_category_id', models.ForeignKey(to='user.Address_Category')),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Education',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('education_description', models.TextField(max_length=255, blank=True)),
                ('school_name', models.CharField(max_length=255, blank=True)),
                ('graduation_status', models.BooleanField(default=False)),
                ('school_year_started', models.DateField(blank=True)),
                ('school_year_ended', models.DateField(blank=True)),
                ('education_category_id', models.ForeignKey(to='user.Education_Category')),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Email',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('email', models.CharField(max_length=50, blank=True)),
                ('email_category_id', models.ForeignKey(to='user.Address_Category')),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Job',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('job_description', models.TextField(max_length=255, blank=True)),
                ('company_name', models.CharField(max_length=50, blank=True)),
                ('company_state_province', models.CharField(max_length=50, blank=True)),
                ('company_country', models.CharField(max_length=50, blank=True)),
                ('company_year_started', models.DateField(blank=True)),
                ('company_year_ended', models.DateField(blank=True)),
                ('job_category_id', models.ForeignKey(to='user.Job_Category')),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('country_code', models.PositiveSmallIntegerField(blank=True)),
                ('phone_number', models.PositiveSmallIntegerField(blank=True)),
                ('phone_category_id', models.ForeignKey(to='user.Phone_Category')),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('skill_description', models.TextField(max_length=255, blank=True)),
                ('skill_category_id', models.ForeignKey(to='user.Skill_Category')),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
        ),
        migrations.CreateModel(
            name='User_Social_Media',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('social_media_url', models.URLField(blank=True)),
                ('social_media_category_id', models.ForeignKey(to='user.Social_Media_Category')),
                ('user_id', models.ForeignKey(to='user.User')),
            ],
        ),
    ]
