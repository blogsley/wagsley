import datetime

from django.db import models
from django.utils.translation import gettext_lazy as _

from wagtail.core.fields import StreamField
from wagtail.admin.edit_handlers import StreamFieldPanel
from wagtail.admin.edit_handlers import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel
from wagtail.core.fields import RichTextField
from modelcluster.contrib.taggit import ClusterTaggableManager

from wagtail.core.blocks import (
    StreamBlock, 
    RichTextBlock,
    TextBlock,
    CharBlock 
)
from wagtail.images.blocks import ImageChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtailmarkdown.blocks import MarkdownBlock

from puput.utils import get_image_model_path


class EntryAbstract(models.Model):
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
        #('markdown', MarkdownBlock(icon="code")),
        ('embed', EmbedBlock(max_width=800, max_height=400))
    ], use_json_field=True)

    tags = ClusterTaggableManager(through='puput.TagEntryPage', blank=True)
    date = models.DateTimeField(verbose_name=_("Post date"), default=datetime.datetime.today)
    header_image = models.ForeignKey(
        get_image_model_path(),
        verbose_name=_('Header image'),
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    categories = models.ManyToManyField('puput.Category', through='puput.CategoryEntryPage', blank=True)
    excerpt = RichTextField(
        verbose_name=_('excerpt'),
        blank=True,
        help_text=_("Entry excerpt to be displayed on entries list. "
                    "If this field is not filled, a truncated version of body text will be used.")
    )
    num_comments = models.IntegerField(default=0, editable=False)
    featured = models.BooleanField(default=False)

    content_panels = [
        MultiFieldPanel(
            [
                FieldPanel('title', classname="title"),
                FieldPanel('featured'),
                FieldPanel('header_image'),
                FieldPanel('body', classname="full"),
                FieldPanel('excerpt', classname="full"),
            ],
            heading=_("Content")
        ),
        MultiFieldPanel(
            [
                FieldPanel('tags'),
                InlinePanel('entry_categories', label=_("Categories")),
                InlinePanel(
                    'related_entrypage_from',
                    label=_("Related Entries"),
                    panels=[PageChooserPanel('entrypage_to')]
                ),
            ],
            heading=_("Metadata")),
    ]

    class Meta:
        abstract = True
