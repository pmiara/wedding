from django.urls import path

from . import views


urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('guest', views.GuestView.as_view(), name='guest'),
    path('ajax/gift/', views.GuestView.validate_gift, name='validate_gift'),
    path('', views.HomeView.as_view(), name='home'),
]
