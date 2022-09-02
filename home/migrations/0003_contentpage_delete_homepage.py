# Generated by Django 4.0 on 2022-09-01 13:58

from django.db import migrations, models
import django.db.models.deletion
import wagtail.blocks
import wagtail.contrib.table_block.blocks
import wagtail.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContentPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('summary', wagtail.fields.RichTextField(blank=True, verbose_name='optional summary/teaser')),
                ('content', wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('htmltext', wagtail.blocks.RawHTMLBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='home/partials/table_template.html')), ('imagetext', wagtail.blocks.StructBlock([('reverse', wagtail.blocks.BooleanBlock(help_text='Image on left? Defaults to right.', required=False)), ('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.BooleanBlock(required=False)), ('third', wagtail.blocks.BooleanBlock(help_text='1:2 split? Default is 1:1', required=False))]))], use_json_field=None)),
                ('extra_info', wagtail.fields.StreamField([('richtext', wagtail.blocks.RichTextBlock()), ('htmltext', wagtail.blocks.RawHTMLBlock()), ('table', wagtail.contrib.table_block.blocks.TableBlock(template='home/partials/table_template.html')), ('imagetext', wagtail.blocks.StructBlock([('reverse', wagtail.blocks.BooleanBlock(help_text='Image on left? Defaults to right.', required=False)), ('text', wagtail.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.blocks.BooleanBlock(required=False)), ('third', wagtail.blocks.BooleanBlock(help_text='1:2 split? Default is 1:1', required=False))]))], blank=True, help_text='Info normally appears on right side, above links', use_json_field=None)),
                ('featured_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.DeleteModel(
            name='HomePage',
        ),
    ]