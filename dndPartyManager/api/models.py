from django.db import models
from django.contrib.auth.models import User as DjangoUser

# Create your models here.

class User(DjangoUser):

    def __str__(self):
        return 'User ' + self.userName

class CharacterClass(models.Model):

    def __str__(self):
        return 'Class ' + self.name

    name = models.CharField(max_length=100, blank=False)

class Ability(models.Model):

    def __str__(self):
        return 'Ability ' + self.name

    class AbilityType(models.TextChoices):
        ARCANE_SPELL = 'Arcane Spell'
        DIVINE_SPELL = 'Divine Spell'
        FEAT = 'Feat'

    name = models.CharField(max_length=200, blank=False)
    description = models.CharField(max_length=1000, blank=False)
    level = models.IntegerField(blank=False)
    abilityType = models.CharField(
        max_length=100,
        choices=AbilityType.choices
    )

class Character(models.Model):

    def __str__(self):
        return 'Character ' + self.name

    name = models.CharField(max_length=100, blank=False)
    level = models.IntegerField(blank=False, default=1)
    characterClass = models.ManyToManyField(CharacterClass)
    abilities = models.ManyToManyField(Ability)
    player = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)

class AbilityUse(models.Model):

    def __str__(self):
        return f'AbilityUse by {self.character.name} of {self.ability.name} at {self.timestamp}'

    ability = models.ForeignKey(Ability, on_delete=models.CASCADE, blank=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=False)
    timestamp = models.DateTimeField(blank=False)