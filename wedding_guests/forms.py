from django import forms
from django.db.models import Q
from django.forms.widgets import CheckboxSelectMultiple

from .models import Guest, Gift


class LoginForm(forms.Form):
    error_msg = 'Nieprawidłowe hasło lub login'
    username = forms.CharField(label='Login')
    password = forms.CharField(label='Hasło', widget=forms.PasswordInput)


class GuestForm(forms.ModelForm):
    class Meta:
        model = Guest
        exclude = ['username', 'is_accompanying_person']

    def __init__(self, *args, **kwargs):
        super(GuestForm, self).__init__(*args, **kwargs)
        guest = kwargs['instance']
        if not guest.is_accompanying_person:
            del self.fields['name']
            del self.fields['surname']

    def as_my_p(self):
        return self._html_output(
            normal_row='<p%(html_class_attr)s data-toggle="tooltip" data-placement="left" title="%(help_text)s">%(label)s %(field)s</p>',
            error_row='%s',
            row_ender='</p>',
            help_text_html='%s',
            errors_on_separate_row=True,
        )


GuestFormSet = forms.modelformset_factory(Guest, form=GuestForm, extra=0)


class GiftForm(forms.Form):
    gifts = forms.MultipleChoiceField()

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(GiftForm, self).__init__(*args, **kwargs)
        self.fields['gifts'].widget = CheckboxSelectMultiple()
        self.fields['gifts'].choices = list(map(lambda g: (g.id, g.name), Gift.objects.filter(Q(user=None) | Q(user=user))))
        self.fields['gifts'].initial = list(map(lambda g: g.id, Gift.objects.filter(user=user)))
        self.fields['gifts'].required = False
        self.taken_gifts = list(map(lambda g: g.name, Gift.objects.exclude(user=None).exclude(user=user)))
