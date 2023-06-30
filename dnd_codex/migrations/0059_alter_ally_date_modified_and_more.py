# Generated by Django 4.2.1 on 2023-06-27 00:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_codex', '0058_alter_ally_date_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ally',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=datetime.datetime(2023, 6, 26, 19, 14, 11, 785961)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 26, 19, 14, 11, 787966)),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 26, 19, 14, 11, 784959)),
        ),
    ]
