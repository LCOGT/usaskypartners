from django.shortcuts import render
from django.views.generic import DetailView

from .models import ContentPage

class HomePage(DetailView):
    model = ContentPage
    template_name = 'home/content_page.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page'] = context['object']
        return context
