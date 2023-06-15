# Generated by Django 4.2.1 on 2023-06-14 04:00

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_codex', '0007_rename_charclass_characterclass_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ally',
            name='damageType',
            field=models.ManyToManyField(help_text='Select a damage type from previous types or create a new one using the + button\n', related_name='%(class)s_characters', to='dnd_codex.damagetype'),
        ),
        migrations.AlterField(
            model_name='ally',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 23, 0, 11, 632074)),
        ),
        migrations.RemoveField(
            model_name='creature',
            name='damageType',
        ),
        migrations.AlterField(
            model_name='creature',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 23, 0, 11, 634077)),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='damageType',
            field=models.ManyToManyField(help_text='Select a damage type from previous types or create a new one using the + button\n', related_name='%(class)s_characters', to='dnd_codex.damagetype'),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 23, 0, 11, 628074)),
        ),
        migrations.AddField(
            model_name='creature',
            name='damageType',
            field=models.ManyToManyField(help_text='Select a damage type from previous types or create a new one using the + button\n', related_name='%(class)s_characters', to='dnd_codex.damagetype'),
        ),
    ]
