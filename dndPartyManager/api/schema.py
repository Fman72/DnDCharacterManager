from graphene import relay, List, Field, String, ObjectType, Schema, Int
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from . import models
from . import serializers
from . import service


class CharacterClassType(DjangoObjectType):
    class Meta:
        model = models.CharacterClass
        fields = ('id', 'name')
        interfaces = (relay.Node, )
        filter_fields = ['name']

class AbilityType(DjangoObjectType):
    class Meta:
        model = models.Ability
        fields = ('id', 'name', 'description', 'level')
        interfaces = (relay.Node, )
        filter_fields = {
            'name': ['icontains', 'istartswith', 'iendswith', 'exact'],
            'level': ['exact'],
        }

class CharacterType(DjangoObjectType):
    class Meta:
        model = models.Character
        fields = ('id', 'name', 'level', 'characterClass', 'player')
        interfaces = (relay.Node, )
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
    class Meta:
        model = models.AbilityUse
        fields = ('ability', 'character', 'timestamp')
        interfaces = (relay.Node, )
        filter_fields = ['character']

class LearnedAbilityType(DjangoObjectType):
    class Meta:
        model = models.LearnedAbility
        fields = ('character', 'ability', 'uses', 'learnedType')
        interfaces = (relay.Node, )
        filter_fields = ['character']

class GameSessionType(DjangoObjectType):
    class Meta:
        model = models.GameSession
        fields = ('code', 'name', 'description', 'historic')
        interfaces = (relay.Node, )

class Query(ObjectType):
    characterClass = relay.Node.Field(CharacterClassType)
    ability = relay.Node.Field(AbilityType)
    character = relay.Node.Field(CharacterType)
    abilityUse = relay.Node.Field(AbilityUseType)
    gameSession = relay.Node.Field(GameSessionType)
    learnedAbility = relay.Node.Field(LearnedAbilityType)

    allCharacterClasses = DjangoFilterConnectionField(CharacterClassType)
    allAbilities = DjangoFilterConnectionField(AbilityType)
    allCharacters = DjangoFilterConnectionField(CharacterType)
    allAbilityUses = DjangoFilterConnectionField(AbilityUseType)
    allLearnedAbilities = DjangoFilterConnectionField(LearnedAbilityType)

    allAbilitiesForClasses = List(AbilityType, classes=List(Int))

    def resolve_allAbilitiesForClasses(root, info, classes):
        return service.getAllAbilitiesForClasses(classes)


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

class GameSessionMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.GameSessionSerializer

class LearnedAbilityMutation(SerializerMutation):
    class Meta:
        convert_choices_to_enum = False
        serializer_class = serializers.LearnedAbilitySerializer

class Mutation(ObjectType):
    character=CharacterMutation.Field()
    abilityUse=AbilityUseMutation.Field()
    gameSession=GameSessionMutation.Field()
    learnedAbility=LearnedAbilityMutation.Field()
