# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20141129_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='orderID',
        ),
        migrations.AddField(
            model_name='order',
            name='id',
            field=models.AutoField(default=None, serialize=False, primary_key=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 4, 12, 27, 21, 431095, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
