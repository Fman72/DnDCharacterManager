from .schemaSubscriptions import AbilityUseSubscription
import logging
from background_task import background

@background(schedule=10)
def sub_test():
  logger = logging.getLogger(__name__)
  logger.critical('test')
  AbilityUseSubscription.broadcast(
    group='test',
    # Dict delivered to the `publish` method.
    payload={
      'abilityUse': {
        'id': 1
      }
    },
  )