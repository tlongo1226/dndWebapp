from django.contrib import admin
from django.contrib import messages
from colorfield.fields import ColorField
from .models import Enemy, Ally, Creature,Race, PlayableClass, DamageType, Subclass, JournalEntry, Event, EventType
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

@admin.register(PlayableClass)
class PlayableClassAdmin(admin.ModelAdmin):
    list_display=('name', 'Instance_Count',)

class SubclassInline(admin.TabularInline):
    models = Subclass
    extra = 0

@admin.register(Subclass)
class SubclassAdmin(admin.ModelAdmin):
    list_display = ('name', 'parentClass',)

@admin.register(DamageType)
class DamageTypeAdmin(admin.ModelAdmin):
    list_display=('name', 'Instance_Count',)

class EventInline(admin.TabularInline):
    model = JournalEntry.events.through
    extra = 1

@admin.register(JournalEntry)
class JournalEntryAdmin(admin.ModelAdmin):
    list_display = ('date',)
    inlines = [EventInline]

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('event_type', 'description')

@admin.register(EventType)
class EventTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'color')

