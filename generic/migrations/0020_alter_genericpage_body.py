# Generated by Django 5.0 on 2024-01-28 20:26

import wagtail.blocks
import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('generic', '0019_alter_genericpage_body'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genericpage',
            name='body',
            field=wagtail.fields.StreamField([('heading', wagtail.blocks.CharBlock(template='heading_block.html')), ('paragraph', wagtail.blocks.RichTextBlock())], null=True, use_json_field=True),
        ),
    ]
