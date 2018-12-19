from django import forms

from .models import Guest, Gift


class LoginForm(forms.Form):
    error_msg = 'Nieprawidłowe hasło lub login'
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


GuestFormSet = forms.modelformset_factory(
    Guest,
    exclude=['username', 'name', 'surname'],
    extra=0
)

class GiftForm(forms.ModelForm):
    class Meta:
        model = Gift
        fields = ['is_reserved']


from django.forms.widgets import CheckboxSelectMultiple


class GiftForm(forms.Form):
    gifts = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(GiftForm, self).__init__(*args, **kwargs)
        self.fields['gifts'].widget = CheckboxSelectMultiple()
        self.fields['gifts'].choices = list(map(lambda g: (g.id, g.name), Gift.objects.all()))
        self.fields['gifts'].initial = list(map(lambda g: g.id, Gift.objects.filter(user=user)))
