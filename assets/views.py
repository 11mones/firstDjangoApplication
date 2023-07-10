from django.shortcuts import render
from django.views.generic import TemplateView
# from assets.views import AboutView


class HomeView(TemplateView):
    template_name= 'home.html'
class Aboutview(TemplateView):
    template_name='aboutus.html'

# Create your views here.
