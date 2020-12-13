from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User


class GameData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    currentGameSession = models.ForeignKey('api.GameSession', null=True, on_delete=models.SET_NULL)
    currentCharacter = models.ForeignKey('api.Character', null=True, on_delete=models.SET_NULL)