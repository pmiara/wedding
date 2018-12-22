from django.contrib.auth.models import User
from django.db import models

import editdistance as ed

STOP_WORDS = ['do', 'w', 'dla', 'na', 'i', 'o', 'we', 'u']
SIMILARITY_THRESHOLD = 0.7


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
    gift = models.CharField(
        'Prezent',
        blank=True,
        max_length=50,
        help_text='''W celu uniknięcia powtarzania się upominków,
                     możesz wpisać tutaj swój prezent.'''
    )
    comments = models.TextField('Dodatkowy komentarz', blank=True, max_length=200)

    @staticmethod
    def get_similar_gifts(gift):
        gifts = Guest.objects.order_by('gift').values_list('gift', flat=True).distinct()
        gift_scores = []
        for old_gift in gifts:
            gift_scores.append((old_gift, Guest.compare_gifts(old_gift, gift)))
        suggestions = map(
            lambda x: x[0],
            filter(lambda x: x[1] > SIMILARITY_THRESHOLD, gift_scores)
        )
        return ', '.join(suggestions)

    @staticmethod
    def compare_gifts(gift1, gift2):
        gift1 = Guest.filter_stop_words(gift1)
        gift2 = Guest.filter_stop_words(gift2)
        scores = [
            1 - ed.eval(w1, w2) / max(len(w1), len(w2)) for w2 in gift2 for w1 in gift1
        ]
        return max(scores)

    @staticmethod
    def filter_stop_words(text):
        return list(filter(lambda w: w not in STOP_WORDS, text.split()))

    def __str__(self):
        return '{} {}'.format(self.name, self.surname)


class Gift(models.Model):
    name = models.CharField('Nazwa', max_length=100)
    is_reserved = models.BooleanField('Zarezerwowany', default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.name
