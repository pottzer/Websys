# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(default=0, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='firstname',
            field=models.CharField(default=0, max_length=30),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='lastname',
            field=models.CharField(default=0, max_length=50),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='user',
            name='ssn',
            field=models.CharField(default=0, max_length=10),
            preserve_default=True,
        ),
    ]
