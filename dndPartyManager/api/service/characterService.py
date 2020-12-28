from api import models

def getCharactersForUser(userId: int):
  query = models.Character.objects.filter(player=userId)
  return query