valor_produto_importado = float(input())

if valor_produto_importado > 2000:
    taxa = (valor_produto_importado - 2000) * 0.2
if valor_produto_importado > 1000 and valor_produto_importado < 2000:
    taxa += 1000 * 0.1
if valor_produto_importado < 1000:
    taxa = 0

print(valor_produto_importado + taxa)
