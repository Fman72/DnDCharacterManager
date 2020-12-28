from api import models

def getCharactersForUser(userId: int) -> QuerySet:
  query = models.Character.objects.filter(player=userId)
  return query