from .. import models

def getOrCreateGameData(user: models.User) -> models.GameData:
    try:
        gameData = models.GameData.objects.get(user=user)
    except models.GameData.DoesNotExist:
        gameData = models.GameData(user=user)
        gameData.save()
    return gameData

def updateGameData(user: models.User, **kwargs) -> models.GameData:
    # need to append _id to set by id.
    fkIdColumns = {}
    for key, value in kwargs.items():
      fkIdColumns[key + '_id'] = value

    gameData = getOrCreateGameData(user)
    gameData = models.GameData(id=gameData.id, **fkIdColumns)
    return gameData