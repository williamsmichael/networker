# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import phonenumber_field.modelfields
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userphone',
            name='country_code',
        ),
        migrations.AlterField(
            model_name='useraddress',
            name='street_address_2',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='school_year_ended',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='usereducation',
            name='school_year_started',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='company_year_ended',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userjob',
            name='company_year_started',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='userphone',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128),
        ),
    ]
