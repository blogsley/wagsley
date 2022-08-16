from wagsley.schema.base import query

from .models import Post
from .schema import PostConnection, PostEdge, PostNode

@query.field("allPosts")
async def resolve_all_posts(root, info, after='', before='', first=0, last=0):
    posts = [p async for p in Post.objects.all()]
    connection = PostConnection(posts)
    result = connection.wire()
    return result


@query.field("post")
def resolve_post(*_, id):
    return Post.objects.aget(id=id)
