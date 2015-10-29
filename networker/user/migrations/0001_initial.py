# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import user.models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('address_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EducationCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('education_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='EmailCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('email_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('job_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkerUser',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('relationship_to_group', models.CharField(max_length=255, blank=True)),
                ('profile_image', models.ImageField(upload_to=user.models.upload_to, blank=True, null=True)),
                ('nickname', models.CharField(max_length=255, blank=True)),
                ('website', models.URLField(blank=True)),
                ('place_of_birth', models.CharField(max_length=255, blank=True)),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('membership_list', models.ManyToManyField(to='group.NetworkerGroup')),
                ('user_extension', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='PhoneCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('phone_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('skill_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('social_media_category', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('street_address_1', models.CharField(max_length=255)),
                ('street_address_2', models.CharField(max_length=255, blank=True)),
                ('city_town', models.CharField(max_length=255)),
                ('state_province', models.CharField(max_length=255)),
                ('postal_code', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('latitude_api', models.FloatField()),
                ('longitude_api', models.FloatField()),
                ('remove', models.BooleanField(default=False)),
                ('address_category_id', models.ForeignKey(to='user.AddressCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('education_title', models.CharField(max_length=255, blank=True)),
                ('education_description', models.TextField(blank=True)),
                ('school_name', models.CharField(max_length=255, blank=True)),
                ('is_completed', models.BooleanField(default=False)),
                ('school_year_started', models.DateField(default=django.utils.timezone.now)),
                ('school_year_ended', models.DateField(default=django.utils.timezone.now)),
                ('remove', models.BooleanField(default=False)),
                ('education_category_id', models.ForeignKey(to='user.EducationCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserEmail',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('email', models.EmailField(max_length=254)),
                ('remove', models.BooleanField(default=False)),
                ('email_category_id', models.ForeignKey(to='user.EmailCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('job_title', models.CharField(max_length=255, blank=True)),
                ('job_description', models.TextField(blank=True)),
                ('company_name', models.CharField(max_length=255, blank=True)),
                ('company_state_province', models.CharField(max_length=255, blank=True)),
                ('company_country', models.CharField(max_length=255, blank=True)),
                ('is_current', models.BooleanField(default=True)),
                ('company_year_started', models.DateField(default=django.utils.timezone.now)),
                ('company_year_ended', models.DateField(default=django.utils.timezone.now)),
                ('remove', models.BooleanField(default=False)),
                ('job_category_id', models.ForeignKey(to='user.JobCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhone',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('country_code', models.PositiveSmallIntegerField(null=True, blank=True)),
                ('phone_number', models.CharField(max_length=255)),
                ('remove', models.BooleanField(default=False)),
                ('phone_category_id', models.ForeignKey(to='user.PhoneCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('skill_description', models.TextField(blank=True)),
                ('remove', models.BooleanField(default=False)),
                ('skill_category_id', models.ForeignKey(to='user.SkillCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserSocialMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('social_media_url', models.URLField()),
                ('remove', models.BooleanField(default=False)),
                ('social_media_category_id', models.ForeignKey(to='user.SocialMediaCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
    ]
