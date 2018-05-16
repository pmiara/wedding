from django.shortcuts import render
from django.views.generic.base import TemplateView
from django.views import View


class Home(TemplateView):
    template_name = 'home.html'
