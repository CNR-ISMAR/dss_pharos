# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0003_question_question_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='recommendation',
            name='case',
            field=models.ForeignKey(default=1, to='dss_pharos.Case'),
            preserve_default=False,
        ),
    ]
