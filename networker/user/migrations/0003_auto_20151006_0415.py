# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20151006_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresscategory',
            name='address_category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='educationcategory',
            name='education_category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='emailcategory',
            name='email_category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='jobcategory',
            name='job_category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='networkeruser',
            name='nickname',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='networkeruser',
            name='place_of_birth',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='networkeruser',
            name='profile_image',
            field=models.ImageField(max_length=255, upload_to='static/images', blank=True),
        ),
        migrations.AlterField(
            model_name='networkeruser',
            name='relationship_to_group',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='phonecategory',
            name='phone_category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='skillcategory',
            name='skill_category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='socialmediacategory',
            name='social_media_category',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='city_town',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='country',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='postal_code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='state_province',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='street_address_1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='street_address_2',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='education_title',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='useremail',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='company_country',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='company_name',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='company_state_province',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='job_title',
            field=models.CharField(max_length=255, blank=True),
        ),
        migrations.AlterField(
            model_name='userphone',
            name='phone_number',
            field=models.CharField(max_length=255),
        ),
    ]
