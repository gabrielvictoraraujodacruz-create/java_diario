# 4) Leia o valor de uma compra. Se o valor for maior que R$ 100, aplique 10% de desconto.
compra = int(input("valor da sua compra: "))
if compra > 100:
    desconto = compra * 0.1  # CORRIGIDO: faltava a indentação dentro do if/else
    valor_final = (compra - desconto)
    print(f"o valor com desconto é:{valor_final}")
else:
    print(f"o valor da sua compra é:{compra}")
