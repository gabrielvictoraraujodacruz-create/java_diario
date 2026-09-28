# Projeto 09: Calculadora de terminal

> Original em Python: [`original.py`](original.py) (dos meus projetos locais de Python)

## Missão

Recriar a calculadora de terminal: ler `10 + 5`, calcular e repetir até digitar `sair`.

## O que muda no Java

- Laço infinito: `while (true) { ... break; }`
- Ler a linha inteira: `String entrada = sc.nextLine().trim();`
- `switch` moderno (Java 14+), que é bem mais limpo que uma escada de `if`:

```java
double resultado = switch (operacao) {
    case "+" -> a + b;
    case "-" -> a - b;
    case "**" -> Math.pow(a, b);
    default -> throw new IllegalArgumentException("Operação inválida");
};
```

- Converter texto em número: `Double.parseDouble(texto)`. Se o texto não for número, dá `NumberFormatException`, que é o `ValueError` do Java.
- ⚠️ `split` do Java usa **regex**, e `entrada.split("+")` quebra. Prefira `entrada.indexOf(op)` e `entrada.substring(...)`.
- 💡 A função `calcular` do original às vezes devolve **número** e às vezes devolve **texto** ("Erro: divisão por zero"). Java não deixa, porque o método tem um tipo de retorno só. O jeito Java é lançar `ArithmeticException` e tratar no `main`.

## Checklist

- [ ] `10 + 5`, `7 / 2`, `2 ** 10` e `10 % 3` funcionam
- [ ] `5 / 0` mostra erro sem fechar o programa
- [ ] `abc + 1` mostra "entrada inválida"
- [ ] `sair` encerra
- [ ] marquei ✅ na tabela da Fase 2 no README principal
- [ ] commit e push

## Rodar

```
cd pratica/projeto-09-calculadora
java Calculadora.java
```
