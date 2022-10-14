from django.core.management.base import BaseCommand

from wagtail.models import Page


class Command(BaseCommand):
    """
    Remove Wagtail welcome page which collides with pages imported
    """

    help = 'Remove Wagtail welcome page which collides with pages imported'

    def handle(self, **options):
        Page.objects.filter(title__contains='Wagtail').delete()
