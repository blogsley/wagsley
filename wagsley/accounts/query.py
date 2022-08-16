from wagsley.schema.base import query
from .models import User
from .schema import UserConnection, UserEdge, UserNode


@query.field("allUsers")
async def resolve_all_users(_, info, after:str=None, before:str=None, first:int=0, last:int=0):
    #users = [u for u in User.objects.all()]
    users = [u async for u in User.objects.all()]
    connection = UserConnection(users)
    result = connection.wire()
    return result


@query.field("user")
def resolve_user(*_, id):
    return User.objects.aget(id=id) #NOTE: You can return a coroutine and Ariadne will run it.  Neat!
