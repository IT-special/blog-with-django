# Generated by Django 2.2.3 on 2019-07-10 15:11

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190124_1800'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 10, 18, 11, 13, 353332), verbose_name='date published'),
        ),
    ]
