from channels.db import database_sync_to_async

from wagsley.schema.base import query

#from .models import Post
from puput.models import EntryPage as Post
from .schema import PostConnection, PostEdge, PostNode

@query.field("allPosts")
@database_sync_to_async
def resolve_all_posts(root, info, after='', before='', first=0, last=0):
    # return Post.objects.all()
    posts = [p for p in Post.objects.all()]
    connection = PostConnection(posts)
    result = connection.wire()
    return result


@query.field("post")
@database_sync_to_async
def resolve_post(*_, id):
    return Post.objects.get(id=id)
