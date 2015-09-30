# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20150930_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useremail',
            name='email_category_id',
            field=models.ForeignKey(to='user.EmailCategory'),
        ),
    ]
