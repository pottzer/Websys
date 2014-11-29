# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_merge'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='expired',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='goods',
            name='id_good',
            field=models.CharField(max_length=32, unique=True, serialize=False, primary_key=True),
            preserve_default=True,
        ),
    ]
