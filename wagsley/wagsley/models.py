from django.db import models
from puput.abstracts import EntryAbstract
from wagtail.admin.edit_handlers import FieldPanel

def default_block():
    return dict() 

class PostAbstract(EntryAbstract):
    block = models.JSONField(default=default_block)

    content_panels = EntryAbstract.content_panels + [
        FieldPanel('block')
    ]

    class Meta:
        abstract = True