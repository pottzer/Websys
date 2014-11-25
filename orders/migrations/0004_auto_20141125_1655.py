# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20141125_1654'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitems',
            old_name='id_goods',
            new_name='productID',
        ),
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 11, 25, 16, 55, 1, 136379, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
