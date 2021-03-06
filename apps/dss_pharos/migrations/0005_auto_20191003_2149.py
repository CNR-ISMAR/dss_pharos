# Generated by Django 2.2.6 on 2019-10-03 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dss_pharos', '0004_auto_20191003_0646'),
    ]

    operations = [
        migrations.AddField(
            model_name='impact',
            name='all_users',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='impact',
            name='impact_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='impact',
            name='impact_name',
            field=models.CharField(max_length=100),
        ),
    ]
