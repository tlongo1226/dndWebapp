from django.db import models
from datetime import datetime

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
    ##TODO need to figure out how to display the number for a inherited classes damage type counts
    # def get_count(self):
    #     character_count = sum(
    #         character.damageType.filter(id=self.id).count()
    #         for character in Character.
    #     )
    #     return character_count

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

#TODO change CharClass to something better for display
class CharacterClass(models.Model):
    name = models.CharField(max_length=50, help_text="Enter a class ")

    def Instance_Count(self):
        character_count = sum(
            character.characterClass.filter(id=self.id).count()
            for character in Enemy.objects.all()
        )
        character_count += sum(
            character.characterClass.filter(id=self.id).count()
            for character in Ally.objects.all()
        )
        character_count += sum(
            character.characterClass.filter(id=self.id).count()
            for character in Creature.objects.all()
        )
        return character_count

    def save(self, *args, **kwargs):
        self.Instance_Count()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

class Character(models.Model):
    race = models.ManyToManyField(Race, help_text="Select a race from previous races or create a new one using the + button\n")
    name = models.CharField(max_length=50)
    characterClass = models.ManyToManyField(CharacterClass, help_text="Enter a class for this character or leave blank if it is not known", blank="True", )
    organization = models.CharField(max_length=100, blank=True)
    description = models.TextField()
    damageType = models.ManyToManyField(DamageType, help_text="Select a damage type from previous types or create a new one using the + button\n", )


    def Classes(self):        
        displayClasses = [characterClass.name for characterClass in self.characterClass.all()[:3]]
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


class Ally(Character):
    
    
    date_modified = models.DateTimeField(datetime.now())
    # TODO add affiliate organiation
    # TODO
    def __str__(self):
        return self.name

class Creature(Character):
    health = models.IntegerField(default =0)
    date_modified = models.DateTimeField(datetime.now())
    def __str__(self):
        return self.name
    
