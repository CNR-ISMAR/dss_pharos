# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0015_auto_20181010_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='bg_information',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
