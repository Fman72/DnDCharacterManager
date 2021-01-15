import graphene
import asyncio

from api import schemaMutations, schemaQueries, schemaSubscriptions
from userAuth import schema as userAuthSchema

class Subscription(schemaSubscriptions.Subscription):
    pass

class Query(schemaQueries.Query, userAuthSchema.Query, graphene.ObjectType):
    pass

class Mutation(schemaMutations.Mutation, userAuthSchema.Mutation, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query, mutation=Mutation, subscription=Subscription)