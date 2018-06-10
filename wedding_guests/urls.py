from django.urls import path

from . import views


urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('guest', views.GuestView.as_view(), name='guest'),
    path('ajax/gift/', views.GuestView.validate_gift, name='validate_gift'),
    path('wedding', views.Wedding.as_view(), name='wedding'),
    path('party', views.Party.as_view(), name='party'),
    path('story', views.Story.as_view(), name='story'),
    path('', views.HomeView.as_view(), name='home'),
]
