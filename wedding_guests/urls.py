from django.urls import path

from . import views


urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('ajax/gift/', views.RSVPView.validate_gift, name='validate_gift'),
    path('wedding', views.Wedding.as_view(), name='wedding'),
    path('wedding_party', views.WeddingParty.as_view(), name='wedding_party'),
    path('accommodation', views.Accommodation.as_view(), name='accommodation'),
    path('rsvp', views.RSVPView.as_view(), name='rsvp'),
    path('', views.HomeView.as_view(), name='home'),
]
