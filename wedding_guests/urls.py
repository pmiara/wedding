from django.urls import path

from . import views


urlpatterns = [
    path('login', views.Login.as_view(), name='login'),
    path('guest', views.Guest.as_view(), name='guest'),
    path('', views.Home.as_view(), name='home')
]
