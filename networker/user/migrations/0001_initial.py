# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('address_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EducationCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('education_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmailCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('job_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkerUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('relationship_to_group', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to=None)),
                ('other_email', models.CharField(max_length=50, unique=True)),
                ('date_of_birth', models.DateTimeField()),
                ('user_timezone', models.DateField(default=django.utils.timezone.now)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('created_dateTime', models.DateTimeField(auto_now_add=True)),
                ('last_login_dateTime', models.DateTimeField(auto_now=True)),
                ('user_extension', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('phone_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('skill_category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('social_media_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('street_address_1', models.CharField(max_length=50)),
                ('street_address_2', models.CharField(max_length=50)),
                ('city_town', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=25)),
                ('latitude_api', models.CharField(max_length=50)),
                ('longitude_api', models.CharField(max_length=50)),
                ('address_category_id', models.ForeignKey(to='user.AddressCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('education_description', models.TextField(max_length=255, blank=True)),
                ('school_name', models.CharField(max_length=255, blank=True)),
                ('graduation_status', models.BooleanField(default=False)),
                ('school_year_started', models.DateField(blank=True)),
                ('school_year_ended', models.DateField(blank=True)),
                ('education_category_id', models.ForeignKey(to='user.EducationCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserEmail',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('email', models.CharField(max_length=50, blank=True)),
                ('email_category_id', models.ForeignKey(to='user.EmailCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('job_description', models.TextField(max_length=255, blank=True)),
                ('company_name', models.CharField(max_length=50, blank=True)),
                ('company_state_province', models.CharField(max_length=50, blank=True)),
                ('company_country', models.CharField(max_length=50, blank=True)),
                ('company_year_started', models.DateField(blank=True)),
                ('company_year_ended', models.DateField(blank=True)),
                ('job_category_id', models.ForeignKey(to='user.JobCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhone',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('country_code', models.PositiveSmallIntegerField(blank=True)),
                ('phone_number', models.PositiveSmallIntegerField(blank=True)),
                ('phone_category_id', models.ForeignKey(to='user.PhoneCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('skill_description', models.TextField(max_length=255, blank=True)),
                ('skill_category_id', models.ForeignKey(to='user.SkillCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserSocialMedia',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('social_media_url', models.URLField(blank=True)),
                ('social_media_category_id', models.ForeignKey(to='user.SocialMediaCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
    ]
