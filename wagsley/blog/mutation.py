from asgiref.sync import sync_to_async

from loguru import logger

from .hub import hub, PostSubscriber, PostEvent

from wagsley.schema.base import mutation
from wagsley.iam.jwt import load_user
from .models import Blog, Post


@mutation.field("createPost")
async def resolve_create_post(_, info, data):
    user = await load_user(info)
    if not user.is_authenticated:
        raise Exception("User not authenticated!")

    title = data.get("title", None)
    block = data.get("block", None)
    body = data.get("body", None)

    blog = await Blog.objects.afirst()
    logger.debug(blog)

    #TODO:Fix this mess
    
    #post = await Post.objects.acreate(title=title, block=block, body=body) #Can't: causes validation error

    post = await sync_to_async(Post)(owner=user, title=title, block=block, body=body)
    await sync_to_async(blog.add_child)(instance=post)
    await sync_to_async(blog.save)()

    logger.debug(post)
    return post


@mutation.field("updatePost")
def resolve_update_post(_, info, id, data):
    user = load_user(info)
    if not user.is_authenticated:
        raise Exception("User not authenticated!")

    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        logger.debug("Post not found")
        raise Exception("Post not found")

    title = data.get("title", None)
    block = data.get("block", None)
    body = data.get("body", None)

    post.title = title
    post.block = block
    post.body = body

    post.save()

    event = PostEvent(id, 'update')

    return event

@mutation.field("deletePost")
def resolve_delete_post(_, info, id):
    user = load_user(info)
    if not user.is_authenticated:
        raise Exception("User not authenticated!")

    try:
        post = Post.objects.get(id=id)
    except Post.DoesNotExist:
        logger.debug("Post not found")
        raise Exception("Post not found")

    post.delete()

    event = PostEvent(id, 'delete')

    return event
