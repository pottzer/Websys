# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id_good', models.CharField(max_length=32, unique=True, serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=64)),
                ('price', models.IntegerField(max_length=32)),
                ('image', models.ImageField(null=True, upload_to=b'pictures', blank=True)),
                ('stock', models.IntegerField(default=0, max_length=32)),
                ('description', models.CharField(max_length=1000)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
