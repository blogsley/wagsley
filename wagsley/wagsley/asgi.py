"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

from ariadne.asgi import GraphQL
from channels.routing import URLRouter
from django.urls import path, re_path
from starlette.middleware.cors import CORSMiddleware

from .schema import schema
from .iam.middleware import TokenAuthMiddleware

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

def get_context_value(request):
    return {
        "request": request,
        "cookies": request.scope.get("cookies", {}),
        "user": request.scope.get("user"),
        "session": request.scope.get("session"),
    }

app = CORSMiddleware(
    GraphQL(schema, debug=True),
    allow_origins=['*'],
    allow_methods=("GET", "POST", "OPTIONS"),
    allow_headers=['access-control-allow-origin', 'authorization', 'content-type']
    )

application = URLRouter(
    [
        #path("graphql/", GraphQL(schema, debug=True, context_value=get_context_value)),
        path("graphql/", app),
        re_path(r"", get_asgi_application()),
    ]
)
'''
application = TokenAuthMiddleware(URLRouter(
    [
        #path("graphql/", GraphQL(schema, debug=True, context_value=get_context_value)),
        path("graphql/", app),
        re_path(r"", get_asgi_application()),
    ]
))
'''
