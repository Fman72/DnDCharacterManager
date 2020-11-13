from rest_framework import serializers
from . import models


class CharacterClassSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.CharacterClass
        fields = ['name']

class AbilitySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Ability
        fields = ['name', 'description', 'level', 'abilityType']

class CharacterSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Character
        fields = ['name', 'level', 'characterClass', 'abilities', 'player']

class AbilityUseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.AbilityUse
        fields = ['ability', 'character', 'timestamp']