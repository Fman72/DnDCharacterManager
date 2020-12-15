from rest_framework import serializers
from . import models

class GameDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.GameData
        fields = [
            'user',
            'currentGameSession',
            'currentCharacter',
        ]
