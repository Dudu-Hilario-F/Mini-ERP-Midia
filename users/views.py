from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def list_users(request):
    return render(request, 'users/list.html')


@login_required
def profile(request):
    return render(request, 'users/profile.html')
