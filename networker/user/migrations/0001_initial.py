# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('address_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='EducationCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('education_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmailCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('email_category', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='JobCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('job_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='NetworkerUser',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('relationship_to_group', models.CharField(max_length=50)),
                ('profile_image', models.ImageField(upload_to='static/images')),
                ('date_of_birth', models.DateField()),
                ('user_extension', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PhoneCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('phone_category', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='SkillCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('skill_category', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='SocialMediaCategory',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('social_media_category', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('street_address_1', models.CharField(max_length=50)),
                ('street_address_2', models.CharField(blank=True, max_length=50)),
                ('city_town', models.CharField(max_length=50)),
                ('state_province', models.CharField(max_length=50)),
                ('country', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=25)),
                ('latitude_api', models.FloatField()),
                ('longitude_api', models.FloatField()),
                ('address_category_id', models.ForeignKey(to='user.AddressCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserEducation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('education_description', models.TextField(blank=True, max_length=255)),
                ('school_name', models.CharField(blank=True, max_length=255)),
                ('is_completed', models.BooleanField(default=False)),
                ('school_year_started', models.DateField(default=django.utils.timezone.now)),
                ('school_year_ended', models.DateField(default=django.utils.timezone.now)),
                ('education_category_id', models.ForeignKey(to='user.EducationCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserEmail',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
                ('email_category_id', models.ForeignKey(to='user.EmailCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserJob',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('job_description', models.TextField(blank=True, max_length=255)),
                ('company_name', models.CharField(blank=True, max_length=50)),
                ('company_state_province', models.CharField(blank=True, max_length=50)),
                ('company_country', models.CharField(blank=True, max_length=50)),
                ('is_current', models.BooleanField(default=True)),
                ('company_year_started', models.DateField(default=django.utils.timezone.now)),
                ('company_year_ended', models.DateField(default=django.utils.timezone.now)),
                ('job_category_id', models.ForeignKey(to='user.JobCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserPhone',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('phone_category_id', models.ForeignKey(to='user.PhoneCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserSkill',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('skill_description', models.TextField(blank=True, max_length=255)),
                ('skill_category_id', models.ForeignKey(to='user.SkillCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserSocialMedia',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('social_media_url', models.URLField()),
                ('social_media_category_id', models.ForeignKey(to='user.SocialMediaCategory')),
                ('user_id', models.ForeignKey(to='user.NetworkerUser')),
            ],
        ),
    ]
