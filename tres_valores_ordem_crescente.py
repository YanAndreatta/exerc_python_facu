# Meu code
# usando as variáveis em pt-br ;d
valor_1 = int(input())
valor_2 = int(input())
valor_3 = int(input())

# Bora pelo caminho mais longo
if valor_1 <= valor_2 and valor_2 <= valor_3:
    print(f"{valor_1} {valor_2} {valor_3}")
elif valor_1 <= valor_3 and valor_3 <= valor_2:
    print(f"{valor_1} {valor_3} {valor_2}")
elif valor_2 <= valor_1 and valor_1 <= valor_3:
    print(f"{valor_2} {valor_1} {valor_3}")
elif valor_2 <= valor_3 and valor_3 <= valor_1:
    print(f"{valor_2} {valor_3} {valor_1}")
elif valor_3 <= valor_1 and valor_1 <= valor_2:
    print(f"{valor_3} {valor_1} {valor_2}")
else:
    print(f"{valor_3} {valor_2} {valor_1}")


# Promtp do Chatgpt (image)
# result
# Solicita ao usuário três valores inteiros positivos
# valores = []

# for i in range(3):
#     valor = int(input(f"Digite o valor {i+1}: "))
#     valores.append(valor)

# # Ordena os valores em ordem crescente
# valores.sort()

# # Exibe os valores ordenados
# print("Valores em ordem crescente:", ' '.join(map(str, valores)))

# Gostei dessa!
