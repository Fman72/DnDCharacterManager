from graphene import relay, List, Field, String, ObjectType, Schema
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from . import models
from . import serializers

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


class CharacterMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.CharacterSerializer
        # lookup_field = 'id'

    @classmethod
    # This sets the player for a character to the logged in user.
    def get_serializer_kwargs(cls, root, info, **input):
        player = info.context.user.id
        data = {**input, 'player': player}
        if 'id' in input:
            instance = Post.objects.filter(id=input['id'], owner=info.context.user).first()
            if instance:
                return {'instance': instance, 'data': data, 'partial': True}

            else:
                raise http.Http404

        return {'data': data, 'partial': True}

class AbilityUseMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.AbilityUseSerializer

class Mutation(ObjectType):
    character=CharacterMutation.Field()
    abilityUse=AbilityUseMutation.Field()