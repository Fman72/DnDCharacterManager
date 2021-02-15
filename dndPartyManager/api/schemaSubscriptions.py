import asyncio
import graphene
import channels_graphql_ws
from .schemaQueries import AbilityUseType
from graphene_django_extras import DjangoObjectField


class AbilityUseSubscription(channels_graphql_ws.Subscription):
    abilityUse = DjangoObjectField(AbilityUseType)

    class Arguments:
        """That is how subscription arguments are defined."""
        gameSessionCode = graphene.String()

    @staticmethod
    def subscribe(root, info, gameSessionCode):
        """Called when user subscribes."""

        # Return the list of subscription group names.
        return ['test']

    @staticmethod
    def publish(payload, info, arg1, arg2):
        """Called to notify the client."""

        # Here `payload` contains the `payload` from the `broadcast()`
        # invocation (see below). You can return `MySubscription.SKIP`
        # if you wish to suppress the notification to a particular
        # client. For example, this allows to avoid notifications for
        # the actions made by this particular client.

        return TestSubscription(event='AbilityUseTest')

class Subscription(graphene.ObjectType):
    """Root GraphQL subscription."""
    abilityUseSubscription = AbilityUseSubscription.Field()