# Meu code
# Ou horas se preferir :p
value_1 = int(input())
value_2 = int(input())
totvalue = 0

if (value_1 == 0):
    value_1 = 24
if (value_2 == 0):
    value_2 = 24

if (value_1 == value_2):
    totvalue = 24
    print(totvalue)
elif (value_1 < value_2):
    totvalue = value_2 - value_1
    print(totvalue)
else:
    totvalue = (24 + value_2) - value_1
    print(totvalue)

# Prompt chatGPT "texto do enunciado"
# result
# Solicitar a entrada do usuário para o horário de início e fim
# hora_inicio = int(input("Informe a hora de início da partida (0 a 24): "))
# hora_fim = int(input("Informe a hora de finalização da partida (0 a 24): "))

# # Calcular a duração da partida
# if hora_inicio < hora_fim:
#     duracao = hora_fim - hora_inicio
# elif hora_inicio > hora_fim:
#     duracao = (24 - hora_inicio) + hora_fim
# else:
#     duracao = 24  # Se o início e o fim forem iguais, a partida durou 24
# horas

# # Exibir o resultado
# print(f"A partida durou {duracao} horas.")

# Esse ficou parecido mesmo hein!
