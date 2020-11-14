from rest_framework import serializers
from django.contrib.auth.models import User
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
    
    characterClass = CharacterClassSerializer(many=True, read_only=True)
    abilities = AbilitySerializer(many=True, required=False, read_only=True)
    # Player is not required here as it is set from the logged in user not the request.
    player = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = models.Character
        fields = ['id', 'name', 'level', 'characterClass', 'abilities', 'player']

class AbilityUseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.AbilityUse
        fields = ['ability', 'character', 'timestamp']