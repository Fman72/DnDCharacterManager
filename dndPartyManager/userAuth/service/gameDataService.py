from .. import models

def getOrCreateGameData(user: models.User) -> models.GameData:
    gameData, created = models.GameData.objects.update_or_create(user=user)
    return gameData

def updateGameData(user: models.User, **kwargs) -> models.GameData:
    # need to append _id to set by id.
    fkIdColumns = {}
    for key, value in kwargs.items():
      fkIdColumns[key + '_id'] = value

    gameData = getOrCreateGameData(user)
    models.GameData.objects.filter(pk=gameData.pk).update(**fkIdColumns)
    gameData.refresh_from_db()
    return gameData