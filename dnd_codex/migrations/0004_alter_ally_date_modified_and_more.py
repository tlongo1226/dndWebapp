# Generated by Django 4.2.1 on 2023-06-13 22:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_codex', '0003_charclass_race_ally_description_ally_organization_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ally',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 17, 50, 3, 649014)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 17, 50, 3, 650015)),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 17, 50, 3, 648015)),
        ),
    ]
