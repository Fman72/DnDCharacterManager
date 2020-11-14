import graphene

from api import schema as apiSchema

class Query(apiSchema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)