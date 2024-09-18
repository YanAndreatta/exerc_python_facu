# Meu code
hora_i = int(input())
min_i = int(input())
hora_f = int(input())
min_f = int(input())
n_hora = 0

if hora_i == 0:
    hora_i = 24
if hora_f == 0:
    hora_f = 24
if min_i == 60:
    min_i = 0
if min_f == 60:
    min_f = 0

if min_i < min_f:
    totalMin = min_f - min_i
elif min_i == min_f:
    totalMin = 0
else:
    totalMin = (60 + min_f) - min_i
    n_hora += 1

if hora_i == hora_f and min_i < min_f:
    totalH = 0
    print(f"{totalH}:{totalMin:02d}")
elif hora_i < hora_f:
    totalH = hora_f - hora_i - n_hora
    print(f"{totalH}:{totalMin:02d}")
else:
    totalH = (24 + hora_f) - hora_i - n_hora
    print(f"{totalH}:{totalMin:02d}")

# promt chatGPT (imagem do enunciado)
# result
# def calcular_duracao(hora_inicio, minuto_inicio, hora_fim, minuto_fim):
#     # Convertendo tudo para minutos
#     inicio_total_minutos = hora_inicio * 60 + minuto_inicio
#     fim_total_minutos = hora_fim * 60 + minuto_fim

#     # Se o fim é menor que o início, a partida passou da meia-noite
#     if fim_total_minutos < inicio_total_minutos:
#         fim_total_minutos += 24 * 60  # Adiciona 24 horas em minutos

#     duracao_total_minutos = fim_total_minutos - inicio_total_minutos

#     # Converte de volta para horas e minutos
#     duracao_horas = duracao_total_minutos // 60
#     duracao_minutos = duracao_total_minutos % 60

#     return f"{duracao_horas}:{duracao_minutos:02d}"


# # Exemplo de uso:
# hora_inicio = int(input("Hora de início: "))
# minuto_inicio = int(input("Minuto de início: "))
# hora_fim = int(input("Hora de fim: "))
# minuto_fim = int(input("Minuto de fim: "))

# duracao = calcular_duracao(hora_inicio, minuto_inicio, hora_fim, minuto_fim)
# print(f"Duração da partida: {duracao}")
# :P
