hora_inicial, minuto_inicial, hora_final, minuto_final = map(int,(input().split()))

horas_totais = hora_final - hora_inicial

if horas_totais == 0:
    horas_totais = 24

minutos_totais = minuto_final - minuto_inicial

diferenca_minutos = minuto_final - minuto_inicial

if minuto_final < minuto_inicial:
    horas_totais = horas_totais - 1
    minutos_totais = 60 + diferenca_minutos

if horas_totais < 0:
    horas_totais = 24 + horas_totais

if horas_totais == 24 and minutos_totais > 0:
    horas_totais = 0 

print(f"O JOGO DUROU {horas_totais} HORA(S) E {minutos_totais} MINUTO(S)")
