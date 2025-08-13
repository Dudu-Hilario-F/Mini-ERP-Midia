from django.shortcuts import render


def list_escalas(request):
    return render(request, 'escalas/list.html')
