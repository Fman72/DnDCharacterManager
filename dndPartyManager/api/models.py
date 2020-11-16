from django.db import models
from django.contrib.auth.models import User

# Create your models here.

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

    name = models.CharField(max_length=200, blank=False, unique=True)
    description = models.CharField(max_length=1000, blank=False)
    level = models.IntegerField(blank=False)
    abilityType = models.CharField(
        max_length=100,
        choices=AbilityType.choices
    )

class GameSession(models.Model):

    def __str__(self):
        return f'GameSession {self.id}'

    name = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=100, blank=True)
    code = models.CharField(max_length=100, blank=False, unique=True)
    historic = models.BooleanField(blank=False, default=False)

class Character(models.Model):

    def __str__(self):
        return 'Character ' + self.name

    name = models.CharField(max_length=100, blank=False)
    level = models.IntegerField(blank=False, default=1)
    characterClass = models.ManyToManyField(CharacterClass)
    player = models.ForeignKey(User, on_delete=models.CASCADE, blank=False)
    currentSession = models.ForeignKey(GameSession, on_delete=models.DO_NOTHING, null=True)

class AbilityUse(models.Model):

    def __str__(self):
        return f'AbilityUse by {self.character.name} of {self.ability.name} at {self.timestamp}'

    ability = models.ForeignKey(Ability, on_delete=models.CASCADE, blank=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=False)
    timestamp = models.DateTimeField(blank=False)

class LearnedAbility(models.Model):

    def __str__(self):
        return f'LearnedAbility by {self.character.name} of {self.ability.name} at {self.timestamp}'

    class LearnedTypes(models.TextChoices):
        WIZARD_SPELL = 'Wizard Spell'
        SORCERER_SPELL = 'Sorcerer Spell'
        CLERIC_SPELL = 'Cleric Spell'
        FEAT = 'Feat'

    ability = models.ForeignKey(Ability, on_delete=models.CASCADE, blank=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, blank=False)
    uses = models.IntegerField(blank=False)
    learnedType = models.CharField(
        max_length=100,
        choices=LearnedTypes.choices
    )
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(ability, character),
    #     ]
    