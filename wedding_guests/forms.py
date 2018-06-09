from django import forms


class LoginForm(forms.Form):
    error_msg = 'Nieprawidłowe hasło lub login'
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)
