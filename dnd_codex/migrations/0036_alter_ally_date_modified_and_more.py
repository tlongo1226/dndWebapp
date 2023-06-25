# Generated by Django 4.2.1 on 2023-06-25 00:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_codex', '0035_alter_ally_date_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ally',
            name='date_modified',
            field=models.DateTimeField(default=datetime.datetime.now, verbose_name=datetime.datetime(2023, 6, 24, 19, 35, 1, 830406)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 24, 19, 35, 1, 832407)),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 24, 19, 35, 1, 828406)),
        ),
    ]
