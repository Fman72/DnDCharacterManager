from graphene import relay, List, Field, String, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from . import models

class CharacterClassType(DjangoObjectType):
    class Meta:
        model = models.CharacterClass
        fields = ('id', 'name')
        interfaces = (relay.Node, )
        filter_fields = ['name']

class AbilityType(DjangoObjectType):
    class Meta:
        model = models.Ability
        fields = ('id', 'name', 'description', 'level', 'abilityType')
        interfaces = (relay.Node, )
        filter_fields = {
            'name': ['icontains', 'istartswith', 'iendswith', 'exact'],
            'level': ['exact'],
            'abilityType': ['exact']
        }

class CharacterType(DjangoObjectType):
    class Meta:
        model = models.Character
        fields = ('id', 'name', 'level', 'characterClass', 'abilties', 'player')
        interfaces = (relay.Node, )
        filter_fields = ['name', 'level', 'characterClass', 'player']

class AbilityUseType(DjangoObjectType):
    class Meta:
        model = models.AbilityUse
        fields = ('ability', 'character', 'timestamp')
        interfaces = (relay.Node, )
        filter_fields = ['ability', 'character', 'timestamp']

class Query(ObjectType):
    characterClass = relay.Node.Field(CharacterClassType)
    ability = relay.Node.Field(AbilityType)
    character = relay.Node.Field(CharacterType)
    abilityUse = relay.Node.Field(AbilityUseType)

    allCharacterClasses = DjangoFilterConnectionField(CharacterClassType)
    allAbilities = DjangoFilterConnectionField(AbilityType)
    allCharacters = DjangoFilterConnectionField(CharacterType)
    allAbilityUses = DjangoFilterConnectionField(AbilityUseType)

schema = Schema(query=Query)