# Dia 03: Desconto na compra

> Original em Python: [`original.py`](original.py) (do repo [programacoes_de_computadores](https://github.com/gabrielvictoraraujodacruz-create/programacoes_de_computadores))

## Missão

Ler o valor de uma compra. Se for maior que R$ 100, aplicar 10% de desconto.

## O que muda no Java

- O original usa `int(input(...))` para dinheiro, e isso **perde os centavos**. Em Java, use `double` e `sc.nextDouble()`.
- Para mostrar com 2 casas decimais:

```java
System.out.printf("Valor final: R$ %.2f%n", valorFinal);
```

`%.2f` é o número com 2 casas e `%n` é a quebra de linha.

- ⚠️ **Pegadinha do Windows em português:** o `Scanner` segue o idioma do sistema, então `nextDouble()` espera **vírgula** (`150,50`). Se você digitar `150.50` e der `InputMismatchException`, é isso. Para aceitar ponto, crie o Scanner assim:

```java
Scanner sc = new Scanner(System.in).useLocale(java.util.Locale.US);
```

## Desafio extra (opcional)

Mostrar também quanto a pessoa economizou.

## Checklist

- [ ] testei com 80, 100, 100,01 e 250,50
- [ ] marquei ✅ na tabela do README principal
- [ ] commit e push

## Rodar

```
cd dia-03-desconto
java Desconto.java
```
