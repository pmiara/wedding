from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.contrib.auth import authenticate, login

from django.views import View


class Home(TemplateView):
    template_name = 'home.html'


class Guest(TemplateView):
    template_name = 'guest.html'


class Login(View):

    def get(self, request):
        return redirect('home')

    def post(self, request):
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('guest')
        else:
            return redirect('home')
