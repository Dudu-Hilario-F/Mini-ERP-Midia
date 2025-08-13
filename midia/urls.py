from django.urls import path
from . import views

app_name = 'midia'

urlpatterns = [
    path('', views.list_midia, name='list'),
]