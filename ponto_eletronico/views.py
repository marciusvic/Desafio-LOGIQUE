from django.shortcuts import render, redirect

from .models import Empresa, CustomUser, PontoEletronico
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from .funcoes import calcular_horas_trabalhadas, calcular_tempo_restante

from django.utils import timezone
import pytz

def home(request):
    if request.user.is_authenticated:
        pontos = PontoEletronico.objects.filter(user_id=request.user.id, data=timezone.now().date()).order_by('hora')
        horas_trabalhadas = calcular_horas_trabalhadas(pontos)
        tempo_restante = calcular_tempo_restante(horas_trabalhadas, request.user.regime_horas)
        print(tempo_restante)
        return render(request, 'usuarios/homeAuthenticated.html', {'pontos': pontos, 'horas_trabalhadas': horas_trabalhadas, 'tempo_restante': tempo_restante})
    else:
        if request.method == 'GET':
            return render(request, 'usuarios/home.html')
        if request.method == 'POST':
            cpf = request.POST.get('cpf')
            senha = request.POST.get('senha')
            cpfexiste = CustomUser.objects.filter(cpf=cpf).exists()
            if not cpfexiste:
                return render(request, 'usuarios/home.html', {'error_message': 'CPF não encontrado'})
            username = CustomUser.objects.get(cpf=cpf).username
            user = authenticate(request, username=username, password=senha)
            
            if user:
                auth_login(request, user)
                return redirect('/')
            else:
                return render(request, 'usuarios/home.html', {'error_message': 'Usuário ou senha inválidos!'})

def logout_view(request):
    logout(request)
    return redirect('/')

def ponto(request):
    if request.method == 'GET':
        return redirect('/')
    else:
        local_time = timezone.localtime(timezone.now())
        fortaleza_tz = pytz.timezone('America/Fortaleza')
        fortaleza_time = local_time.astimezone(fortaleza_tz)
        hora = fortaleza_time.time()
        data = fortaleza_time.date()
        user_id = request.user.id
        
        ponto_eletronico = PontoEletronico(user_id=user_id, data=data, hora=hora)
        ponto_eletronico.save()
        return redirect('/')