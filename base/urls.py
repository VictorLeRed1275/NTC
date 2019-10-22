from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('join/', views.member, name='member'),
    path('join-guide/', views.guide, name='guide'),
    path('administration/', views.admin, name='admin'),
    path('calendar/new/', views.calendar_new, name='calendar_new'),
    path('calendar/', views.calendar, name='calendar'),
    path('event/new/', views.event_new, name='event_new'),
    path('event/', views.event, name='event'),
    path('event/<pk>/remove/', views.event_remove, name='event_remove'),
]