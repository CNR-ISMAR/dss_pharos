# Generated by Django 2.0.13 on 2019-11-02 20:58

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0010_auto_20191102_1936'),
    ]

    operations = [
        migrations.AlterField(
            model_name='description',
            name='textContent',
            field=ckeditor.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='description',
            name='textView',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]