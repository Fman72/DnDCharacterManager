from graphene import List, Field, String, ObjectType, Schema, Int, Interface
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django_extras import DjangoObjectField, DjangoFilterListField
from . import models
from . import serializers
from .service import abilityService, gameSessionService

class SpellCasterTarget(Interface):

    name = String()

    @classmethod
    def resolve_type(cls, instance, info):
        if instance.__class__.__name__ == 'Character':
            return CharacterType

class CharacterClassType(DjangoObjectType):
    class Meta:
        model = models.CharacterClass
        filter_fields = ['name']

class AbilityType(DjangoObjectType):
    class Meta:
        model = models.Ability
        filter_fields = {
            'name': ['icontains', 'istartswith', 'iendswith', 'exact'],
            'level': ['exact'],
        }

class CharacterType(DjangoObjectType):
    class Meta:
        model = models.Character
        interfaces = (SpellCasterTarget, )
        filter_fields = ['id', 'name', 'level', 'characterClass', 'player']

        @classmethod
        def get_node(cls, info, id):
            try:
                character = Character.objects.get(id=id)
            except Character.DoesNotExist:
                return None

            if character.player == info.context.user:
                return character
            return None

class AbilityUseType(DjangoObjectType):
    caster = Field(SpellCasterTarget)
    target = Field(SpellCasterTarget)
    
    class Meta:
        model = models.AbilityUse
        filter_fields = ['gameSession']

class LearnedAbilityType(DjangoObjectType):
    class Meta:
        model = models.LearnedAbility
        filter_fields = ['character']

class GameSessionType(DjangoObjectType):
    class Meta:
        model = models.GameSession

class Query(ObjectType):
    characterClass = DjangoObjectField(CharacterClassType)
    ability = DjangoObjectField(AbilityType)
    character = DjangoObjectField(CharacterType)
    abilityUse = DjangoObjectField(AbilityUseType)
    gameSession = DjangoObjectField(GameSessionType)
    learnedAbility = DjangoObjectField(LearnedAbilityType)

    allCharacterClasses = DjangoFilterListField(CharacterClassType)
    allAbilities = DjangoFilterListField(AbilityType)
    allCharacters = DjangoFilterListField(CharacterType)
    allAbilityUses = DjangoFilterListField(AbilityUseType)
    allLearnedAbilities = DjangoFilterListField(LearnedAbilityType)

    allAbilitiesForClasses = List(AbilityType, classes=List(Int))

    def resolve_allAbilitiesForClasses(root, info, classes):
        return abilityService.getAllAbilitiesForClasses(classes)


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