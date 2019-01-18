from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.contrib import messages


from .forms import LoginForm, GuestFormSet, GiftForm
from .models import Guest, Gift


class HomeView(View):

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
            else:
                login_form.add_error(None, login_form.error_msg)

        return render(request, 'home.html', {'login_form': login_form})


class RSVPView(LoginRequiredMixin, View):

    def get(self, request, active_tab=0):
        guests = Guest.objects.filter(username=request.user)
        formset = GuestFormSet(queryset=guests)
        gift_form = GiftForm(user=request.user)
        gift_urls = {gift.id: gift.url for gift in Gift.objects.all()}
        if 0 > active_tab or active_tab > len(formset):
            active_tab = 0
        return render(request, 'rsvp.html',
            {'formset': formset, 'gift_form': gift_form, 'gift_urls': gift_urls, 'active_tab': active_tab})

    def post(self, request, active_tab=0):
        formset = GuestFormSet(request.POST)
        gift_form = GiftForm(request.POST, user=request.user)
        if formset.is_valid() and gift_form.is_valid():
            formset.save()
            chosen_gift_ids = gift_form.cleaned_data['gifts']
            Gift.objects.filter(user=request.user).update(user=None)
            Gift.objects.filter(id__in=chosen_gift_ids).update(user=request.user)
            messages.success(request, 'Poprawna aktualizacja formularza')
        return redirect('rsvp_tab_active', active_tab)


def logout_view(request):
    logout(request)
    return redirect('home')


class Wedding(TemplateView):
    template_name = 'wedding.html'


class WeddingParty(TemplateView):
    template_name = 'wedding_party.html'


class Accommodation(TemplateView):
    template_name = 'accommodation.html'
