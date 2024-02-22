from django.shortcuts import render, redirect

from .models import Empresa, CustomUser
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login

from django.utils import timezone

def home(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/homeAuthenticated.html')
    else:
        if request.method == 'GET':
            return render(request, 'usuarios/home.html')
        if request.method == 'POST':
            cpf = request.POST.get('cpf')
            senha = request.POST.get('senha')

            username = CustomUser.objects.get(cpf=cpf).username
            password = senha
            user = authenticate(request, username=username, password=password)

            if user:
                auth_login(request, user)
                return redirect('/')
            else:
                return render(request, 'usuarios/home.html', {'error_message': 'Usuário ou senha inválidos!'})

def logout_view(request):
    logout(request)
    return redirect('/')
