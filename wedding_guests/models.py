from django.contrib.auth.models import User
from django.db import models
from django.utils.translation import gettext_lazy as _


class Guest(models.Model):
    YES, NO, MAYBE = 'Yes', 'No', 'Maybe'
    ATTENDING_STATUSES = (
        (YES, _('Tak')),
        (NO, _('Nie')),
        (MAYBE, _('Nie określono'))
    )
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(_('Imię'), max_length=30)
    surname = models.CharField(_('Nazwisko'), max_length=50)
    attending = models.CharField(
        _('Będę na weselu'), max_length=len(MAYBE), default=MAYBE, choices=ATTENDING_STATUSES
    )
    attending_afters = models.CharField(
        _('Będę na poprawinach'), max_length=len(MAYBE), default=MAYBE, choices=ATTENDING_STATUSES,
        help_text=_('Więcej informacji w zakładce Ślub i Wesele')
    )
    wants_bus = models.BooleanField(
        _('Chcę jechać busem'),
        default=False,
        help_text=_('Więcej informacji w zakładce dojazd.')
    )
    is_vegetarian = models.BooleanField(
        _('Preferuję dania wegetariańskie'),
        default=False,
        help_text=_('Informacja ta pomoże nam przy wyborze menu')
    )
    comments = models.TextField(_('Dodatkowy komentarz'), blank=True, max_length=200)
    is_accompanying_person = models.BooleanField(default=False)
    eligible_for_afters = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)


class Gift(models.Model):
    name = models.CharField('Nazwa', max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
