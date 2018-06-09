from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout

from .forms import LoginForm


class Home(View):

    def get(self, request):
        login_form = LoginForm()
        return render(request, 'home.html', {'login_form': login_form})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data['username']
            password = login_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('guest')
            else:
                login_form.add_error(None, login_form.error_msg)

        return render(request, 'home.html', {'login_form': login_form})


class Guest(TemplateView):
    template_name = 'guest.html'


def logout_view(request):
    logout(request)
    return redirect('home')
