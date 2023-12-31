# Generated by Django 4.2.1 on 2023-06-15 02:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_codex', '0014_alter_ally_damagetype_alter_ally_date_modified_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='damagetype',
            name='instance_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ally',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 14, 21, 37, 10, 643882)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 14, 21, 37, 10, 645903)),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 14, 21, 37, 10, 641914)),
        ),
    ]
