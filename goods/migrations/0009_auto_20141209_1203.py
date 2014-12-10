# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goods', '0008_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('rating', models.CharField(default=b'5', max_length=1, choices=[(b'5', b'5'), (b'4', b'4'), (b'3', b'3'), (b'2', b'2'), (b'1', b'1')])),
                ('productID', models.ForeignKey(to='goods.Goods')),
                ('userID', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='review',
            unique_together=set([('userID', 'productID')]),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2014, 12, 9, 12, 3, 41, 667014, tzinfo=utc)),
            preserve_default=True,
        ),
    ]
