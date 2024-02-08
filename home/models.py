from django.db import models

from wagtail.models import Page
from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField
from wagtail import blocks


class HomePage(Page):
    banner_title = models.CharField(max_length=100, default='Welcome to my homepage!')

    main_image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=False,
        on_delete=models.SET_NULL, 
        related_name='+', 
    )

    secondary_image = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=False,
        on_delete=models.SET_NULL, 
        related_name='+', 
    )

    body = StreamField ([
        #('name', blocks.SomethingBlock()) StreamField comes from Wagtail
        ('heading', blocks.CharBlock(template="heading_block.html")),
        # ('image', ImageChooserBlock()),
        ('paragraph', blocks.RichTextBlock()),
    ], use_json_field=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("main_image"),
        FieldPanel("secondary_image"),
        FieldPanel("body"),
    ]
