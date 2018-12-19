from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse


from .forms import LoginForm, GuestFormSet, GiftForm
from .models import Guest, Page, Gift


class HomeView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('guest')
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


class GuestView(LoginRequiredMixin, View):

    def get(self, request):
        guests = Guest.objects.filter(username=request.user)
        formset = GuestFormSet(queryset=guests)
        gift_form = GiftForm(user=request.user)
        return render(request, 'guest.html', {'formset': formset, 'gift_form': gift_form})

    def post(self, request):
        formset = GuestFormSet(request.POST)
        gift_form = GiftForm(request.POST, user=request.user)
        if formset.is_valid() and gift_form.is_valid():
            formset.save()
            chosen_gift_ids = gift_form.cleaned_data['gifts']
            Gift.objects.filter(user=request.user).update(user=None)
            Gift.objects.filter(id__in=chosen_gift_ids).update(user=request.user)
        return redirect('guest')

    def validate_gift(request):
        similar_gifts = Guest.get_similar_gifts(request.GET.get('gift'))
        return JsonResponse(similar_gifts, safe=False)


def logout_view(request):
    logout(request)
    return redirect('home')


class Wedding(TemplateView):
    template_name = 'wedding.html'


class WeddingParty(TemplateView):
    template_name = 'wedding_party.html'


class Accommodation(TemplateView):
    template_name = 'accommodation.html'
