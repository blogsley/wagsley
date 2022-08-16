from loguru import logger

from channels.db import database_sync_to_async
from channels.auth import AuthMiddlewareStack
from django.contrib.auth.models import AnonymousUser
from django.db import close_old_connections

from .jwt import decode_auth_token
from accounts.models import User

class TokenAuthMiddleware:

    def __init__(self, app):
        self.app = app

    @database_sync_to_async
    def get_user(self, id):
        user = User.objects.get(id=id)
        close_old_connections()
        return user

    async def __call__(self, scope, receive, send):
        token = decode_auth_token(scope)
        if token:
            logger.debug(f'TokenAuthMiddleware:__call__:token:  {token}')
            user = await self.get_user(token["id"])
        else:
            user = AnonymousUser()
        scope['user'] = user
        return await self.app(scope, receive, send)

TokenAuthMiddlewareStack = lambda app: TokenAuthMiddleware(AuthMiddlewareStack(app))
