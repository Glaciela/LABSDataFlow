from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render

def index(request):
    """
    View que lida com o login do usuário.
    Redireciona para o dashboard se o usuário já estiver autenticado.
    """
    if request.user.is_authenticated:
        return redirect('core:dashboard')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('core:dashboard')
        else:
            messages.error(request, 'Usuário ou senha inválidos.')
            return render(request, 'core/index.html')

    return render(request, 'core/index.html')