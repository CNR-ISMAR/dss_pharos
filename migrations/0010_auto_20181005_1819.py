# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0009_auto_20181001_1424'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'ordering': ['question_level']},
        ),
        migrations.AddField(
            model_name='recommendation',
            name='title',
            field=models.CharField(default='Titolo', max_length=20),
            preserve_default=False,
        ),
    ]
