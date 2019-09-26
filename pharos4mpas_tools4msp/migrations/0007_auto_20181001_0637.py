# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0006_auto_20180918_0759'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Case',
            new_name='Activity',
        ),
        migrations.RenameField(
            model_name='activity',
            old_name='case_description',
            new_name='activity_description',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='case',
            new_name='activity',
        ),
        migrations.RenameField(
            model_name='recommendation',
            old_name='case',
            new_name='activity',
        ),
        migrations.AlterField(
            model_name='collection',
            name='condition',
            field=models.CharField(default=b'OR', max_length=3, choices=[(b'AND', b'AND'), (b'OR', b'OR'), (b'NOT', b'NOT')]),
        ),
    ]
