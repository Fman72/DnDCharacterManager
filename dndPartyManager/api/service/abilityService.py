from api import models
from django.db.models.query import QuerySet

# Houses business logic for API module. Basically only thing that isn't boilerplate :/

def getAllAbilitiesForClasses(classIds: List[int]) -> QuerySet:
    querySets = []
    for classId in classIds:
        query = models.Ability.objects.filter(characterClasses__id=classId)
        querySets.append(query)

    allQuery = models.AbilityClass.objects.none()
    for query in querySets:
        allQuery = allQuery.union(query)

    return allQuery