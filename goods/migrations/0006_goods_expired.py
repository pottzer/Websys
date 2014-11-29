# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_remove_goods_expired'),
    ]

    operations = [
        migrations.AddField(
            model_name='goods',
            name='expired',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
