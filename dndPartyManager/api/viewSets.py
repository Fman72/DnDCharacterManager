from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from . import models
from . import serializers


class CharacterClassViewSet(viewsets.ModelViewSet):
    queryset = models.CharacterClass.objects.all()
    serializer_class = serializers.CharacterClassSerializer
    
class AbilityViewSet(viewsets.ModelViewSet):
    queryset = models.Ability.objects.all()
    serializer_class = serializers.AbilitySerializer

class CharacterViewSet(viewsets.ModelViewSet):
    queryset = models.Character.objects.all()
    serializer_class = serializers.CharacterSerializer

class AbilityUseViewSet(viewsets.ModelViewSet):
    queryset = models.AbilityUse.objects.all()
    serializer_class = serializers.AbilityUseSerializer

