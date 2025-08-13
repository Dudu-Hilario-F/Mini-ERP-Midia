from django.shortcuts import render


def list_agenda(request):
    return render(request, 'agenda/list.html')
