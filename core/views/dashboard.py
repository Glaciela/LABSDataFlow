from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def dashboard(request):
    """
    View para o painel principal após o login.
    Acessível apenas para usuários autenticados.
    """
    return render(request, 'core/dashboard.html')