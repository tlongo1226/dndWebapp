from django.contrib import admin
from django.contrib import messages
from .models import Enemy, Ally, Creature,Race, CharacterClass, DamageType
# Register your models here.

@admin.register(Ally)
class AllyAdmin(admin.ModelAdmin):
    list_display=('name', 'Classes', 'Races', 'Damage_Types')

@admin.register(Enemy)
class EnemyAdmin(admin.ModelAdmin):
    list_display=('name', 'Classes', 'Races')
    

@admin.register(Creature)
class CreatureAdmin(admin.ModelAdmin):
    list_display=('name', 'Classes', 'Races')

@admin.register(Race)
class RaceAdmin(admin.ModelAdmin):
    list_display=('name', 'Instance_Count',)

@admin.register(CharacterClass)
class CharacterClassAdmin(admin.ModelAdmin):
    list_display=('name', 'Instance_Count',)


@admin.register(DamageType)
class DamageTypeAdmin(admin.ModelAdmin):
    list_display=('name', 'Instance_Count',)