from django import forms

RACES =[
        ("DB","Dragonborn"),
        ("DW","Dwarf"),
        ("EF","Elf"),
        ("GN","Gnome"),
        ("HE","Half-Elf"),
        ("HF","Halfling"),
        ("HO","Half-Orc"),
        ("HU","Human"),
        ("TF","Tiefling"),
        ("CH", "Changling"),
        ("CL", "Colossus"),
    ]

class enemyForm(forms.Form):
    enemy_name = forms.CharField(label="Name", max_length=100)
    enemy_race = forms.CharField(label="Race", max_length=50, )
