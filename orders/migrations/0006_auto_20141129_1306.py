# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0005_auto_20141129_1103'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderitems',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 29, 13, 6, 9, 314193, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
