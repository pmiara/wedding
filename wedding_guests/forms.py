from django import forms

from .models import Guest


class LoginForm(forms.Form):
    error_msg = 'Nieprawidłowe hasło lub login'
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


GuestFormSet = forms.modelformset_factory(Guest, exclude=['username'], extra=0)
