# Generated by Django 4.2.1 on 2023-06-14 04:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_codex', '0009_alter_ally_damagetype_alter_ally_date_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ally',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 23, 4, 45, 475177)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 23, 4, 45, 477177)),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 23, 4, 45, 473177)),
        ),
    ]
