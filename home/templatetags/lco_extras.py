from bs4 import BeautifulSoup
from datetime import timedelta, datetime
from django import template
from django.conf import settings
from django.db.models import Q
from django.templatetags.static import static
from django.urls import reverse
from django.utils.safestring import mark_safe
from random import choice
from wagtail.rich_text import expand_db_html
from wagtail.images.models import Image
from wagtail.models import Locale

import logging
import os

logger = logging.getLogger(__name__)

register = template.Library()


@register.filter
def teaser(text):
    cleantext = BeautifulSoup(text).text
    sentences = cleantext.split(". ")
    teasertext = ". ".join(sentences[0:2])
    if len(teasertext) > 100:
        return sentences[0]
    else:
        return teasertext

@register.simple_tag
def htmlblock(name):
    try:
        html = HTMLBlock.objects.get(name=name)
        return mark_safe(html.text)
    except:
        return ''

@register.filter
def betterhtml(html):
    return mark_safe(expand_db_html(html))
