def calcular(a, b, operacao):
    if operacao == '+':
        return a + b
    elif operacao == '-':
        return a - b
    elif operacao == '*':
        return a * b
    elif operacao == '/':
        if b == 0:
            return "Erro: divisão por zero"
        return a / b
    elif operacao == '**':
        return a ** b
    elif operacao == '%':
        if b == 0:
            return "Erro: divisão por zero"
        return a % b


def main():
    print("=" * 30)
    print("       CALCULADORA PYTHON")
    print("=" * 30)
    print("Operações: + | - | * | / | ** | %")
    print("Digite 'sair' para encerrar")
    print("=" * 30)

    while True:
        print()
        entrada = input("Expressão (ex: 10 + 5): ").strip()

        if entrada.lower() == 'sair':
            print("Encerrando calculadora.")
            break

        # tenta separar os dois operandos e o operador
        operadores = ['**', '+', '-', '*', '/', '%']
        operacao = None
        partes = None

        for op in operadores:
            if op in entrada:
                partes = entrada.split(op, 1)
                if len(partes) == 2:
                    operacao = op
                    break

        if not operacao:
            print("Entrada inválida. Use o formato: número operador número")
            continue

        try:
            a = float(partes[0].strip())
            b = float(partes[1].strip())
        except ValueError:
            print("Entrada inválida. Certifique-se de usar números válidos.")
            continue

        resultado = calcular(a, b, operacao)

        if isinstance(resultado, str):
            print(resultado)
        else:
            # exibe como inteiro se não tiver casas decimais
            if resultado == int(resultado):
                print(f"Resultado: {int(resultado)}")
            else:
                print(f"Resultado: {resultado}")


if __name__ == "__main__":
    main()
