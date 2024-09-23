qtd_pessoas = int(input())
qtd_lugares_veiculo_9 = 36
qtd_lugares_veiculo_5 = 30

if qtd_pessoas > qtd_lugares_veiculo_9 + qtd_lugares_veiculo_5:
    saida = "-"
else:
    if qtd_pessoas <= qtd_lugares_veiculo_9:
        saida = f"{(qtd_pessoas + 8) // 9}-0"
        # if qtd_pessoas % 9 != 0:
        #     saida = f"{qtd_pessoas // 9 + 1}-0"
        # else:
        #     saida = f"{qtd_pessoas // 9}-0"
    elif qtd_pessoas > qtd_lugares_veiculo_9:
        restante = qtd_pessoas - qtd_lugares_veiculo_9
        saida = f"{qtd_lugares_veiculo_9 // 9}-{(restante + 4) // 5}"
        # if restante % 5 != 0:
        #     saida = f"{qtd_lugares_veiculo_9 // 9}-{restante // 5 + 1}"
        # else:
        #     saida = f"{qtd_lugares_veiculo_9 // 9}-{restante // 5}"


print(saida)
