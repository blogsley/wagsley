import asyncio

from loguru import logger

from wagsley.schema.base import subscription
from .hub import hub, PostSubscriber

@subscription.source("post")
async def events_generator(obj, info, id=None):
    logger.debug(f'events_generator:begin:id {id}')
    subscriber = PostSubscriber(int(id))
    hub.subscribe(subscriber)
    while subscriber.active:
        event = await subscriber.receive()
        logger.debug(f'events_generator:while:  {event}')
        yield event

@subscription.field("post")
def events_resolver(event, info, id=None):
    logger.debug(f'events_resolver:while:  {event}')
    return event
