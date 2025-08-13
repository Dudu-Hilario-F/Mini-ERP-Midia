from django.shortcuts import render


def dashboard(request):
    context = {
        'total_users': 0,
        'escalas_ativas': 0,
        'eventos_hoje': 0,
        'notificacoes_pendentes': 0,
        'proximos_eventos': [],
        'escalas_semana': [],
    }
    return render(request, 'core/dashboard.html', context)
