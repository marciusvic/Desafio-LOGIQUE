from datetime import datetime, timedelta
from django.utils import timezone
import pytz

def formatar_horario(horario):
    tempo_base = datetime(1900, 1, 1) + horario
    return tempo_base.strftime('%H:%M')

def calcular_horas_trabalhadas(pontos):
    local_time = timezone.localtime(timezone.now())
    fortaleza_tz = pytz.timezone('America/Fortaleza')
    fortaleza_time = local_time.astimezone(fortaleza_tz)

    total_trabalhado = timedelta()
    if len(pontos) % 2 == 0:
        for i in range(0, len(pontos), 2):
            entrada = datetime.combine(datetime.today(), pontos[i].hora)
            saida = datetime.combine(datetime.today(), pontos[i + 1].hora)
            total_trabalhado += saida - entrada
    else:
        array_horas = [ponto.hora for ponto in pontos]
        array_horas.append(fortaleza_time.time())
        for i in range(0, len(array_horas), 2):
            entrada = datetime.combine(datetime.today(), array_horas[i])
            saida = datetime.combine(datetime.today(), array_horas[i + 1])
            total_trabalhado += saida - entrada
            
    return formatar_horario(total_trabalhado)

def calcular_tempo_restante(horas_trabalhadas, regime):
    if regime == 8:
        tempo_regime = datetime.strptime('08:00', '%H:%M')
    else:
        tempo_regime = datetime.strptime('06:00', '%H:%M')
    
    horas_trabalhadas = datetime.strptime(horas_trabalhadas, '%H:%M')
    
    tempo_restante = tempo_regime - horas_trabalhadas
    return formatar_horario(tempo_restante)
