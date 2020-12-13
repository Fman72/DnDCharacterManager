import graphene

from api import schema as apiSchema
from userAuth import schema as userAuthSchema

class Query(apiSchema.Query, userAuthSchema.Query, graphene.ObjectType):
    pass

class Mutation(apiSchema.Mutation, userAuthSchema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)