from django.urls import path
from . import views

app_name = 'users'

urlpatterns = [
    path('', views.list_users, name='list'),
    path('perfil/', views.profile, name='profile'),
]