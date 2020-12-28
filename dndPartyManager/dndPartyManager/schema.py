import graphene

from api import schemaMutations, schemaQueries
from userAuth import schema as userAuthSchema

class Query(schemaQueries.Query, userAuthSchema.Query, graphene.ObjectType):
    pass

class Mutation(schemaMutations.Mutation, userAuthSchema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation)