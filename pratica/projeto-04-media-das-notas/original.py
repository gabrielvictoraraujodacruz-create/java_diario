# 5) Leia duas notas, calcule a média e informe:
#    Aprovado (média >= 7), Recuperação (média >= 5 e < 7), Reprovado (média < 5)
nota1 = int(input("digite a nota1: "))
nota2 = int(input("digite a nota2 "))

nota_final = (nota1 + nota2) / 2

if nota_final >= 7:
    print("aprovado")
elif nota_final >= 5:
    print("recuperação")
else:
    print("reprovado")
