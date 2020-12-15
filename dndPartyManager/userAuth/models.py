from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import User


class GameData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    currentGameSession = models.ForeignKey('api.GameSession', null=True, on_delete=models.SET_NULL)
    currentCharacter = models.ForeignKey('api.Character', null=True, on_delete=models.SET_NULL)

    # Django Graphene doesn't show user models in the client side schema, this also prevents showing sensitive user data in client.
    @property
    def userId(self):
        return self.user.id