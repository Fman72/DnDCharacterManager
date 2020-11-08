from django.http import QueryDict

def queryDictToDict(queryDict: QueryDict) -> dict:
    output = {}
    for item in queryDict:
        output[item] = queryDict[item]

    return output