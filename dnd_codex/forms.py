from django import forms
from .models import Ally, Enemy, Creature
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

class enemyForm(forms.ModelForm):
    class Meta:
        model = Enemy
        fields = ['name', 'organization', 'description']


class AllyForm(forms.ModelForm):
    class Meta:
        model = Ally
        fields = ['name', 'organization', 'description']

class CreatureForm(forms.ModelForm):
    class Meta:
        model = Creature
        fields = ['name', 'organization', 'description']