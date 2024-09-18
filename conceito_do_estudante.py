# Meu code
# Dessa vez variáveis em pt-br
nota_1 = float(input())
nota_2 = float(input())
nota_3 = float(input())

media = (nota_1 + (nota_2*2) + (nota_3*3)) / (1 + 2 + 3)

if media < 4:
    print(f"{media:.2f} Reprovado")
elif media >= 4 and media < 7:
    print(f"{media:.2f} Exame")
else:
    print(f"{media:.2f} Reprovado")

# Prompt chatGPT (imagem do enunciado)
# Result
# Solicitando as notas das três provas
# nota1 = float(input("Nota da primeira prova: "))
# nota2 = float(input("Nota da segunda prova: "))
# nota3 = float(input("Nota da terceira prova: "))

# # Calculando a média ponderada
# media = (nota1 * 1 + nota2 * 2 + nota3 * 3) / 6

# # Determinando o conceito
# if media < 4:
#     conceito = "Reprovado"
# elif 4 <= media < 7:
#     conceito = "Exame"
# else:
#     conceito = "Aprovado"

# # Exibindo a média e o conceito
# print(f"{media:.2f} {conceito}")
