from django.shortcuts import render


def list_notificacoes(request):
    return render(request, 'notificacoes/list.html')
