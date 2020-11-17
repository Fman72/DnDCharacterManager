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

class GameSessionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.GameSession
        fields = ['name', 'description', 'code', 'historic']

class CharacterSerializer(serializers.ModelSerializer):
    
    characterClass = CharacterClassSerializer(many=True, read_only=True)
    # Player is not required here as it is set from the logged in user not the request.
    # The schema of this serializer is what SerializerMutations from graphene use.
    # If this is required here we must pass player to the graphql api when making a character which does not make sense as 
    # it is set on the server.
    player = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), required=False)

    class Meta:
        model = models.Character
        fields = ['id', 'name', 'level', 'characterClass', 'player']

class AbilityUseSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.AbilityUse
        fields = ['ability', 'character', 'timestamp']

class LearnedAbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.LearnedAbility
        fields = ['character', 'ability', 'uses', 'learnedType']