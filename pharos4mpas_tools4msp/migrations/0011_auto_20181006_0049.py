# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0010_auto_20181005_1819'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collection',
            name='condition',
        ),
        migrations.AddField(
            model_name='recommendation',
            name='condition',
            field=models.CharField(default=b'OR', max_length=3, choices=[(b'AND', b'AND'), (b'OR', b'OR'), (b'NOT', b'NOT')]),
        ),
    ]
