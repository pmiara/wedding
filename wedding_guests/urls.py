from django.urls import path

from . import views


urlpatterns = [
    path('logout', views.logout_view, name='logout'),
    path('wedding', views.Wedding.as_view(), name='wedding'),
    path('commute', views.Commute.as_view(), name='commute'),
    path('accommodation', views.Accommodation.as_view(), name='accommodation'),
    path('contact', views.Contact.as_view(), name='contact'),
    path('rsvp', views.RSVPView.as_view(), name='rsvp'),
    path('rsvp/<int:active_tab>/', views.RSVPView.as_view(), name='rsvp_tab_active'),
    path('', views.HomeView.as_view(), name='home'),
]
