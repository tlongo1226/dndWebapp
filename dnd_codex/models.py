from django.db import models
from datetime import datetime

class EventType(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20, help_text="Enter a color code for this event type")

    def __str__(self):
        return self.name

class DamageType(models.Model):
    name = models.CharField(max_length=75, help_text="Enter a Damage Type")

    def Instance_Count(self):
        character_count = sum(
            character.damageType.filter(id=self.id).count()
            for character in Enemy.objects.all()
        )
        character_count += sum(
            character.damageType.filter(id=self.id).count()
            for character in Ally.objects.all()
        )
        character_count += sum(
            character.damageType.filter(id=self.id).count()
            for character in Creature.objects.all()
        )
        return character_count

    def save(self, *args, **kwargs):
        self.Instance_Count()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]
    
class Race(models.Model):
    name = models.CharField(max_length=50, help_text="Enter a race/species")

    def Instance_Count(self):
        character_count = sum(
            character.race.filter(id=self.id).count()
            for character in Enemy.objects.all()
        )
        character_count += sum(
            character.race.filter(id=self.id).count()
            for character in Ally.objects.all()
        )
        character_count += sum(
            character.race.filter(id=self.id).count()
            for character in Creature.objects.all()
        )
        return character_count

    def save(self, *args, **kwargs):
        self.Instance_Count()
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name
    class Meta:
        ordering = ["name"]


class PlayableClass(models.Model):
    name = models.CharField(max_length=50, help_text="Enter a class ")

    def Instance_Count(self):
        character_count = sum(
            character.playableClass.filter(id=self.id).count()
            for character in Enemy.objects.all()
        )
        character_count += sum(
            character.playableClass.filter(id=self.id).count()
            for character in Ally.objects.all()
        )
        character_count += sum(
            character.playableClass.filter(id=self.id).count()
            for character in Creature.objects.all()
        )
        return character_count

    def save(self, *args, **kwargs):
        self.Instance_Count()
        super().save(*args, **kwargs)

    def __str__(self):   
        return self.name
    
    class Meta:
        ordering = ["name"]


class Subclass(models.Model):
    name = models.CharField(max_length=50, help_text="Enter a subclass ")
    parentClass = models.ForeignKey( 
        'PlayableClass',
        on_delete=models.CASCADE,
        related_name='subclasses'
    )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ["name"]


class Character(models.Model):
    race = models.ManyToManyField(Race, help_text="Select a race from previous races or create a new one using the + button\n")
    name = models.CharField(max_length=50)
    playableClass = models.ManyToManyField(PlayableClass, help_text="Enter a class for this character or leave blank if it is not known", blank="True", )
    organization = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    damageType = models.ManyToManyField(DamageType, help_text="Select a damage type from previous types or create a new one using the + button\n", null=True, blank=True)

    def Classes(self):
        displayClasses = [playableClass.name for playableClass in self.playableClass.all()[:3]]
        if(len(displayClasses)>3):

            ', '.join(displayClasses)
            displayClasses+="..."
        else:
            ', '.join(displayClasses)
        return displayClasses

    def Races(self):        
        dsiplayRaces = [race.name for race in self.race.all()[:3]]
        if(len(dsiplayRaces)>3):

            ', '.join(dsiplayRaces)
            dsiplayRaces+="..."
        else:
            ', '.join(dsiplayRaces)
        return dsiplayRaces

    def Damage_Types(self):        
        displayDamage = [damage.name for damage in self.damageType.all()[:3]]
        if(len(displayDamage)>3):

            ', '.join(displayDamage)
            displayDamage+="..."
        else:
            ', '.join(displayDamage)
        return displayDamage

    class Meta:
        abstract =True

"""
   Enemies will be characters met during the players travels who are likely to be encountered again
   or might be characters that have importance to the story 
"""
class Enemy(Character):
    # TODO add affiliate organiation
    # TODO Bounty?
    date_modified = models.DateTimeField(datetime.now())
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural='Enemies'

class Ally(Character):
    date_modified = models.DateTimeField(datetime.now(), default=datetime.now)
    # TODO add affiliate organiation

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Allies'

class Creature(Character):
    health = models.IntegerField(default =0)
    date_modified = models.DateTimeField(datetime.now())
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Creatures'

class Event(models.Model):
    event_type = models.ForeignKey(EventType, on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description


class JournalEntry(models.Model):
    date = models.DateField()
    events = models.ManyToManyField(Event)
    enemies = models.ManyToManyField(Enemy, blank=True)
    allies = models.ManyToManyField(Ally, blank=True)

    def __str__(self):
        return f"Journal Entry for {self.date}"
    
    class Meta:
        ordering = ["date"]