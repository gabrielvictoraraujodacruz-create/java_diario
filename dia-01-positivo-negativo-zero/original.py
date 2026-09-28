# 1) Leia um número inteiro e informe se ele é positivo, negativo ou zero.
numero = int(input("escolher numero:"))

if numero > 0:
    print(f"numero é positivo.")
elif numero < 0:
    print(f"numero é negativo.")
else:
    print(f"numero é zero.")

print(f"O resultado é: {numero}")
