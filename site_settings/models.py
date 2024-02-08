from django.db import models
from wagtail.admin.panels import FieldPanel
from wagtail.contrib.settings.models import BaseSiteSetting, register_setting


@register_setting
class SocialMediaSettings (BaseSiteSetting):
    instagram = models.URLField(max_length=100, blank=True)
    facebook = models.URLField(max_length=100, blank=True)
    youtube = models.URLField(max_length=100, blank=True)

    instagram_icon = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=False,
        on_delete=models.SET_NULL, 
        related_name='+', 
    )

    facebook_icon = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=False,
        on_delete=models.SET_NULL, 
        related_name='+', 
    )

    youtube_icon = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=False,
        on_delete=models.SET_NULL, 
        related_name='+', 
    )

    panels = [
        FieldPanel("instagram"),
        FieldPanel("instagram_icon"),
        FieldPanel("facebook"),
        FieldPanel("facebook_icon"),
        FieldPanel("youtube"),
        FieldPanel("youtube_icon"),
    ]

@register_setting
class Hero (BaseSiteSetting):
    
    hero_one = models.ForeignKey(
        'wagtailimages.Image', 
        null=True,
        blank=False,
        on_delete=models.SET_NULL, 
        related_name='+', 
    )

    panels = [
        FieldPanel("hero_one"),
    ]
