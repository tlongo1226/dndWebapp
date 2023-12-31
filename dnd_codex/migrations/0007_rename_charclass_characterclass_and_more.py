# Generated by Django 4.2.1 on 2023-06-14 03:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_codex', '0006_ally_damagetype_enemy_damagetype_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CharClass',
            new_name='CharacterClass',
        ),
        migrations.RenameField(
            model_name='ally',
            old_name='charClass',
            new_name='characterClass',
        ),
        migrations.RenameField(
            model_name='creature',
            old_name='charClass',
            new_name='characterClass',
        ),
        migrations.RenameField(
            model_name='enemy',
            old_name='charClass',
            new_name='characterClass',
        ),
        migrations.AlterField(
            model_name='ally',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 22, 32, 23, 343357)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 22, 32, 23, 345353)),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 22, 32, 23, 342354)),
        ),
    ]
