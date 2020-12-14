from .. import models

def updateGameData(user, **kwargs):
    gameData = models.GameData.objects.get(user=user)
    gameData = models.GameData(id=gameData.id, **kwargs)
    return gameData