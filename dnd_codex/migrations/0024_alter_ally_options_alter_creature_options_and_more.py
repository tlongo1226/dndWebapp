# Generated by Django 4.2.1 on 2023-06-15 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_codex', '0023_alter_ally_options_alter_creature_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ally',
            options={'verbose_name_plural': 'Allies'},
        ),
        migrations.AlterModelOptions(
            name='creature',
            options={'verbose_name_plural': 'Creatures'},
        ),
        migrations.AlterField(
            model_name='ally',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 14, 22, 35, 52, 970772)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 14, 22, 35, 52, 971772)),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 14, 22, 35, 52, 968772)),
        ),
    ]