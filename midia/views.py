from django.shortcuts import render


def list_midia(request):
    return render(request, 'midia/list.html')
