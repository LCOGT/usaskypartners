from wagtail.models import Locale, Page

def menuitems(request):
    menus = Page.objects.filter(locale=Locale.get_active()).live().in_menu()
    return {"menuitems" : menus}
