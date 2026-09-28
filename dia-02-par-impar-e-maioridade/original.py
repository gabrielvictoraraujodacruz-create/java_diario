# ===== ex2_par_ou_impar.py =====
# 2) Leia um número inteiro e verifique se ele é par ou ímpar.
numero = int(input("digitar numero: "))
if numero % 2 == 0:
    print(f"O número {numero} é par.")  # CORRIGIDO: faltava a indentação dentro do if/else
else:
    print(f"O número {numero} é impar.")


# ===== ex3_maior_de_idade.py =====
# 3) Leia a idade de uma pessoa e informe se ela é maior ou menor de idade (18 anos).
idade = int(input("Digite sua idade:"))
if idade < 18:  # CORRIGIDO: era <= 18, e quem tem 18 já é maior de idade
    print(f"É menor de idade")
else:
    print(f"É maior de idade")
