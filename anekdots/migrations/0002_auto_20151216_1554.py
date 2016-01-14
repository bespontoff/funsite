# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('anekdots', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='alias',
            field=models.CharField(max_length=80, default='raznoe'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grade',
            name='grades',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
