# Generated by Django 5.0 on 2024-01-18 03:20

import wagtail.blocks
import wagtail.fields
import wagtail.images.blocks
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0016_genericpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(template='heading_block.html')), ('image', wagtail.images.blocks.ImageChooserBlock()), ('paragraph', wagtail.blocks.RichTextBlock())], null=True, use_json_field=True),
        ),
    ]
