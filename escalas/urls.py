from django.urls import path
from . import views

app_name = 'escalas'

urlpatterns = [
    path('', views.list_escalas, name='list'),
]