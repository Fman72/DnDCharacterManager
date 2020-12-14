import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django_extras import DjangoObjectField, DjangoFilterListField
from . import models
from . import serializers
from .service import gameDataService

class GameDataType(DjangoObjectType):
    class Meta:
        model = models.GameData
        fields = ('id', 'currentGameSession', 'currentCharacter', 'user')
       
class Query(graphene.ObjectType):
    gameData = graphene.Field(GameDataType)
    
    def resolve_gameData(root, info, **kwargs):
        currentUser = info.context.user.id
        gameData = models.GameData.objects.get(user=currentUser)
        return gameData

class GameDataMutation(graphene.Mutation):
    class Arguments:
        currentGameSession = graphene.ID()
        currentCharacter = graphene.ID()

    gameData = graphene.Field(GameDataType)

    @classmethod
    def mutate(cls, root, info, **kwargs):
        currentUser = info.context.user.id
        gameData = gameDataService.updateGameData(currentUser, **kwargs)
        return GameDataMutation(gameData=gameData)

class Mutation(graphene.ObjectType):
    setGameData=GameDataMutation.Field()