# Generated by Django 4.2.1 on 2023-06-14 04:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dnd_codex', '0013_alter_ally_date_modified_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ally',
            name='damageType',
            field=models.ManyToManyField(help_text='Select a damage type from previous types or create a new one using the + button\n', to='dnd_codex.damagetype'),
        ),
        migrations.AlterField(
            model_name='ally',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 23, 9, 43, 971206)),
        ),
        migrations.AlterField(
            model_name='creature',
            name='damageType',
            field=models.ManyToManyField(help_text='Select a damage type from previous types or create a new one using the + button\n', to='dnd_codex.damagetype'),
        ),
        migrations.AlterField(
            model_name='creature',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 23, 9, 43, 973205)),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='damageType',
            field=models.ManyToManyField(help_text='Select a damage type from previous types or create a new one using the + button\n', to='dnd_codex.damagetype'),
        ),
        migrations.AlterField(
            model_name='enemy',
            name='date_modified',
            field=models.DateTimeField(verbose_name=datetime.datetime(2023, 6, 13, 23, 9, 43, 969206)),
        ),
    ]