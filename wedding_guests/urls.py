from django.urls import path

from . import views


urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('guest', views.Guest.as_view(), name='guest'),
    path('', views.Home.as_view(), name='home'),
]
