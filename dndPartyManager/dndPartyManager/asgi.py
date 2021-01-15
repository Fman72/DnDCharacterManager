"""
ASGI config for dndPartyManager project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dndPartyManager.settings')

django.setup()

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from .consumers import MyGraphqlWsConsumer
from asgiref import compatibility

# strangers on github are my heroes
# https://github.com/django/channels/issues/1319
class CustomSocketioProtocolTypeRouter(ProtocolTypeRouter):
    """
    Overrided base class's __call__ method to support python socketio 4.2.0 and daphne 2.3.0
    """
    def __call__(self, scope, *args):
        if scope["type"] in self.application_mapping:
            handlerobj = self.application_mapping[scope["type"]](scope)
            if args:
                return handlerobj(*args)
            return handlerobj
        raise ValueError(
            "No application configured for scope type %r" % scope["type"]
        )


application = ProtocolTypeRouter({
    'http': get_asgi_application(),
    'websocket': URLRouter([
        django.urls.path('graphql/', MyGraphqlWsConsumer),
    ])
})
