import graphene
from graphene_django import DjangoObjectType
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.rest_framework.mutation import SerializerMutation
from graphene_django_extras import DjangoObjectField, DjangoFilterListField
from . import models
from . import serializers

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

class GameDataMutation(SerializerMutation):
    class Meta:
        serializer_class = serializers.GameDataSerializer

    @classmethod
    # Always return the gamedata for the logged in user.
    def get_serializer_kwargs(cls, root, info, **input):
        currentUser = info.context.user.id
        data = {**input, 'player': player}
        if 'id' in input:
            instance = GameData.objects.filter(user=currentUser).first()
            if instance:
                return {'instance': instance, 'data': data, 'partial': True}

            else:
                raise http.Http404

        return {'data': data, 'partial': True}
      
class Mutation(graphene.ObjectType):
    gameData=GameDataMutation.Field()