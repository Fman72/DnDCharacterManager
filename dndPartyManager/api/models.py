from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class CharacterClass(models.Model):

    def __str__(self):
        return 'Class ' + self.name

    name = models.CharField(max_length=100, null=False)

class Ability(models.Model):

    def __str__(self):
        return 'Ability ' + self.name

    class AbilityType(models.TextChoices):
        ARCANE_SPELL = 'Arcane Spell'
        DIVINE_SPELL = 'Divine Spell'
        FEAT = 'Feat'

    name = models.CharField(max_length=200, null=False, unique=True)
    description = models.CharField(max_length=5000, null=False)
    range = models.CharField(max_length=200, null=True)
    components = models.CharField(max_length=200, null=True)
    ritual = models.BooleanField(null=False, default=False)
    duration = models.CharField(max_length=200, null=True)
    concentration = models.BooleanField(null=False, default=False)
    castingTime = models.CharField(max_length=200, null=True)
    level = models.IntegerField(null=False)
    school = models.CharField(max_length=200, null=True)
    spellClass = models.CharField(max_length=200, null=True)
    material = models.CharField(max_length=1000, null=True)
    oaths = models.CharField(max_length=200, null=True)
    patrons = models.CharField(max_length=200, null=True)
    higherLevel = models.CharField(max_length=5000, null=True)
    domains = models.CharField(max_length=200, null=True)
    circles = models.CharField(max_length=200, null=True)
    archetype = models.CharField(max_length=200, null=True)

class AbilityClass(models.Model):

    def __str__(self):
        return 'AbilityClass ' + self.id

    ability = models.ForeignKey(Ability, on_delete=models.CASCADE, null=False)
    characterClass = models.ForeignKey(CharacterClass, on_delete=models.CASCADE, null=False)

class GameSession(models.Model):

    def __str__(self):
        return f'GameSession {self.id}'

    name = models.CharField(max_length=100, null=False)
    description = models.CharField(max_length=100, null=True)
    code = models.CharField(max_length=100, null=False, unique=True)
    historic = models.BooleanField(null=False, default=False)

class Character(models.Model):

    def __str__(self):
        return 'Character ' + self.name

    name = models.CharField(max_length=100, null=False)
    level = models.IntegerField(null=False, default=1)
    characterClass = models.ManyToManyField(CharacterClass)
    player = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    currentSession = models.ForeignKey(GameSession, on_delete=models.DO_NOTHING, null=True)

class AbilityUse(models.Model):

    def __str__(self):
        return f'AbilityUse by {self.character.name} of {self.ability.name} at {self.timestamp}'

    ability = models.ForeignKey(Ability, on_delete=models.CASCADE, null=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=False)
    timestamp = models.DateTimeField(null=False)

class LearnedAbility(models.Model):

    def __str__(self):
        return f'LearnedAbility by {self.character.name} of {self.ability.name} at {self.timestamp}'

    class LearnedType(models.TextChoices):
        WIZARD_SPELL = 'Wizard Spell'
        SORCERER_SPELL = 'Sorcerer Spell'
        CLERIC_SPELL = 'Cleric Spell'
        FEAT = 'Feat'

    ability = models.ForeignKey(Ability, on_delete=models.CASCADE, null=False)
    character = models.ForeignKey(Character, on_delete=models.CASCADE, null=False)
    uses = models.IntegerField(null=False)
    learnedType = models.CharField(
        max_length=100,
        choices=LearnedType.choices
    )
    # class Meta:
    #     constraints = [
    #         models.UniqueConstraint(ability, character),
    #     ]
    