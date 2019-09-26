# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0002_auto_20180916_0929'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_level',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
