from graphene import List, Field, String, ObjectType, Schema, Int, Interface
from graphene_django import DjangoObjectType, DjangoListObjectType
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

class UserListType(DjangoListObjectType):
    class Meta:
        description = " Type definition for user list "
        model = User
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="-username")

class CharacterListType(DjangoListObjectType):
    class Meta:
        model = models.Character
        pagination = LimitOffsetGraphqlPagination(default_limit=25, ordering="name")


class Query(ObjectType):
    characterClass = DjangoObjectField(CharacterClassType)
    ability = DjangoObjectField(AbilityType)
    character = DjangoObjectField(CharacterType)
    abilityUse = DjangoObjectField(AbilityUseType)
    gameSession = DjangoObjectField(GameSessionType)
    learnedAbility = DjangoObjectField(LearnedAbilityType)

    usersCharacters = DjangoListObjectField(CharacterType, extra_filter_meta=)

    allCharacterClasses = DjangoFilterListField(CharacterClassType)
    allAbilities = DjangoFilterListField(AbilityType)
    
    allAbilityUses = DjangoFilterListField(AbilityUseType)
    allLearnedAbilities = DjangoFilterListField(LearnedAbilityType)

    allAbilitiesForClasses = List(AbilityType, classes=List(Int))

    def resolve_allAbilitiesForClasses(root, info, classes):
        return abilityService.getAllAbilitiesForClasses(classes)

    def resolve_usersCharacters(root, info, classes):
        userId = info.context.user.id
        return characterService.getCharactersForUser(userId)
