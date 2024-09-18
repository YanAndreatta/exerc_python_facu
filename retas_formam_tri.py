# meu code - fazer pelo caminho mais longo ;D
value_1 = int(input())
value_2 = int(input())
value_3 = int(input())

modulo_1 = (value_2 - value_3)  # | b - c |
modulo_2 = (value_1 - value_3)  # | a - c |
modulo_3 = (value_1 - value_2)  # | a - b |

if modulo_1 < 0:
    modulo_1 = modulo_1 * -1
if modulo_2 < 0:
    modulo_2 = modulo_2 * -1
if modulo_3 < 0:
    modulo_3 = modulo_3 * -1

result = "não"

if modulo_1 < value_1 and (value_2 + value_3) > value_1:
    result = "sim"
if modulo_2 < value_2 and (value_1 + value_3) > value_2:
    result = "sim"
if modulo_3 < value_3 and (value_1 + value_2) > value_3:
    result = "sim"

print(result)

# prompt do chatgpt (image)
# result
# Função para verificar se três segmentos podem formar um triângulo
# def verifica_triangulo(a, b, c):
#     if a + b > c and a + c > b and b + c > a:
#         return "sim"
#     else:
#         return "não"


# # Solicitando ao usuário os três valores
# a = int(input("Informe o valor do primeiro segmento: "))
# b = int(input("Informe o valor do segundo segmento: "))
# c = int(input("Informe o valor do terceiro segmento: "))

# # Verificando se os segmentos podem formar um triângulo
# resultado = verifica_triangulo(a, b, c)

# # Exibindo o resultado
# print(resultado)

# Ele fez com funções, pedi para fazer sem funções
# Solicitando ao usuário os três valores
# a = int(input("Informe o valor do primeiro segmento: "))
# b = int(input("Informe o valor do segundo segmento: "))
# c = int(input("Informe o valor do terceiro segmento: "))

# # Verificando se os segmentos podem formar um triângulo
# if a + b > c and a + c > b and b + c > a:
#     print("sim")
# else:
#     print("não")
