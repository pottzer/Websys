# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_auto_20141204_1255'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(default=b'nameless', max_length=30)),
                ('comment_text', models.CharField(max_length=1024)),
                ('date', models.DateTimeField(default=datetime.datetime(2014, 12, 4, 13, 38, 56, 965073, tzinfo=utc))),
                ('productID', models.ForeignKey(to='goods.Goods')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
