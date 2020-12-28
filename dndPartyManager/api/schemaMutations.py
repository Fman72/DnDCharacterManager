from graphene import List, Field, String, ObjectType, Schema, Int, Interface
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django_extras import DjangoObjectField, DjangoFilterListField
from . import models
from . import serializers
from .service import abilityService, gameSessionService

class CharacterMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.CharacterSerializer

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

class GameSessionMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.GameSessionSerializer
        model_operations = ['create']

    @classmethod
    # This generates a random code for new game sessions.
    def get_serializer_kwargs(cls, root, info, **input):
        data = {**input, 'code': gameSessionService.generateCode()}
        return {'data': data, 'partial': True}

class LearnedAbilityMutation(SerializerMutation):
    class Meta:
        convert_choices_to_enum = False
        serializer_class = serializers.LearnedAbilitySerializer

class Mutation(ObjectType):
    character=CharacterMutation.Field()
    abilityUse=AbilityUseMutation.Field()
    gameSession=GameSessionMutation.Field()
    learnedAbility=LearnedAbilityMutation.Field()