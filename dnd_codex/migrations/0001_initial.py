# Generated by Django 4.2.1 on 2023-06-07 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ally',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(choices=[('DB', 'Dragonborn'), ('DW', 'Dwarf'), ('EF', 'Elf'), ('GN', 'Gnome'), ('HE', 'Half-Elf'), ('HF', 'Halfling'), ('HO', 'Half-Orc'), ('HU', 'Human'), ('TF', 'Tiefling')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Creature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('health', models.IntegerField(default=0)),
                ('damageType', models.CharField(choices=[('AC', 'Acid'), ('BG', 'Bludgeoning'), ('CD', 'Cold'), ('FR', 'Fire'), ('FO', 'Force'), ('LG', 'Lightning'), ('NE', 'Necrotic'), ('PI', 'Piercing'), ('PY', 'Psychic'), ('RA', 'Radiant'), ('SL', 'Slashing'), ('TH', 'Thundering'), ('PO', 'Poison')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Enemy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('race', models.CharField(choices=[('DB', 'Dragonborn'), ('DW', 'Dwarf'), ('EF', 'Elf'), ('GN', 'Gnome'), ('HE', 'Half-Elf'), ('HF', 'Halfling'), ('HO', 'Half-Orc'), ('HU', 'Human'), ('TF', 'Tiefling')], max_length=30)),
            ],
        ),
    ]