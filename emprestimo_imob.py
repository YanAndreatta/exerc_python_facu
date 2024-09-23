valor_imovel = float(input())
renda_mensal = float(input())
tempo_ano = int(input())

result = valor_imovel / (tempo_ano * 12)

if result <= renda_mensal * 0.3:
    print(f"{result:.2f}")
else:
    print("Recusado")
