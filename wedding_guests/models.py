from django.contrib.auth.models import User
from django.db import models


class Guest(models.Model):
    YES, NO, MAYBE = 'Yes', 'No', 'Maybe'
    ATTENDING_STATUSES = (
        (YES, 'Tak'),
        (NO, 'Nie'),
        (MAYBE, 'Nie określono')
    )
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField('Imię', max_length=30)
    surname = models.CharField('Nazwisko', max_length=50)
    attending = models.CharField(
        'Będę na weselu', max_length=len(MAYBE), default=MAYBE, choices=ATTENDING_STATUSES
    )
    wants_bus = models.BooleanField(
        'Chcę jechać autobusem',
        default=False,
        help_text='''Zapewniamy dojazd spod kościoła na salę weselną zaraz po mszy
        i z powrotem do Poznania na koniec wesela (koło 4 w nocy).'''
    )
    is_vegetarian = models.BooleanField(
        'Preferuję dania wegetariańskie',
        default=False,
        help_text='Informacja ta pomoże nam przy wyborze menu'
    )
    gift = models.CharField('Prezent', blank=True, max_length=50)
    comments = models.TextField('Dodatkowy komentarz', blank=True, max_length=200)

    @staticmethod
    def get_similar_gifts(gift):
        return ', '.join([gift, 'czołg', 'odrzutowiec'])

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)
