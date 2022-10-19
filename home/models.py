from bs4 import BeautifulSoup
from django.core.paginator import Paginator
from django.db import models

from wagtail.admin.panels import FieldPanel
from wagtail.blocks import StreamBlock, StructBlock
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.fields import RichTextField, StreamField
from wagtail.images.blocks import ImageChooserBlock
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.models import Page, Locale
from wagtail.search import index

from wagtail import blocks

def stream_teaser(content, title):
    if content:
        html = content[0].value.source
        soup = BeautifulSoup(html, 'html.parser')
        txt = soup.text
        if len(txt) > 200:
            txt = f"{txt[0:200]}..."
        return txt
    else:
        return f"{title} on Las Cumbres Observatory"


class ImageText(StructBlock):
    reverse = blocks.BooleanBlock(help_text='Image on left? Defaults to right.', required=False)
    text = blocks.RichTextBlock()
    image = ImageChooserBlock()
    caption = blocks.BooleanBlock(required=False)
    third = blocks.BooleanBlock(help_text="1:2 split? Default is 1:1", required=False)

class BodyBlock(StreamBlock):
    richtext = blocks.RichTextBlock()
    htmltext = blocks.RawHTMLBlock()
    table =  TableBlock(template="home/partials/table_template.html")
    imagetext = ImageText()

class ContentPage(Page):
    summary = RichTextField("optional summary/teaser", blank=True)
    content = StreamField(BodyBlock, use_json_field=True)
    extra_info = StreamField(BodyBlock, help_text ="Info normally appears on right side, above links", blank=True, use_json_field=True)
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )

    content_panels = Page.content_panels + [
        FieldPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('content'),
        FieldPanel('extra_info'),
    ]

class NewsPage(Page):
    parent_page_types = ['NewsIndexPage']
    featured_image = models.ForeignKey(
        'wagtailimages.Image',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='+'
    )
    summary = models.CharField("Optional teaser", max_length=250, blank=True)
    content = StreamField(BodyBlock, use_json_field=True)

    search_fields = Page.search_fields + [
        index.SearchField('teaser'),
        index.SearchField('content'),
    ]

    content_panels = Page.content_panels + [
        ImageChooserPanel('featured_image'),
        FieldPanel('summary'),
        FieldPanel('content'),
    ]

    parent_page_types = ['home.NewsIndexPage']

    @property
    def display_date(self):
        if self.go_live_at:
            return self.go_live_at
        else:
            return self.first_published_at

    @property
    def teaser(self):
        if self.summary:
            return self.summary
        else:
            return stream_teaser(self.content, self.title)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blog_list = NewsPage.objects.filter(locale=Locale.get_active()).live().order_by('-go_live_at')
        context['newspages'] = blog_list
        return context


class NewsIndexPage(Page):
    description = RichTextField(blank=True)

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        blog_list = NewsPage.objects.filter(locale=Locale.get_active()).live().order_by('-go_live_at')
        paginator = Paginator(blog_list, 20)
        page = request.GET.get('page')
        blogpages = paginator.get_page(page)
        context['blogpages'] = blogpages
        return context

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]
    parent_page_types = ['home.ContentPage','home.HomePage']

class HomePage(Page):
    tagline = RichTextField("short description", blank=True)
    about = RichTextField("about project", blank=True)
    content = StreamField(BodyBlock, use_json_field=True)

    content_panels = Page.content_panels + [
        FieldPanel('tagline'),
        FieldPanel('about'),
        FieldPanel('content'),
    ]

    def get_context(self, request):
        # Update context to include only published posts, ordered by reverse-chron
        context = super().get_context(request)
        context['news'] = NewsPage.objects.live().order_by('-go_live_at')[2]
        return context
