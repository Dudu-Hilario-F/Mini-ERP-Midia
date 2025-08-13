from django.urls import path
from . import views

app_name = 'agenda'

urlpatterns = [
    path('', views.list_agenda, name='list'),
]