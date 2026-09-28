# Dia 02: Par ou ímpar + maior de idade

> Original em Python: [`original.py`](original.py) (do repo [programacoes_de_computadores](https://github.com/gabrielvictoraraujodacruz-create/programacoes_de_computadores))

## Missão

Dois programas curtos, um em cada arquivo:

1. `ParOuImpar.java`: ler um inteiro e dizer se é par ou ímpar.
2. `MaiorDeIdade.java`: ler a idade e dizer se a pessoa é maior ou menor de idade.

## O que muda no Java

- O `%` funciona igual ao do Python.
- Java tem o tipo `boolean` (`true`/`false`, com minúscula). Dá para guardar a condição numa variável:

```java
boolean ehPar = numero % 2 == 0;
if (ehPar) { ... }
```

- ⚠️ No original, o ex3 começou com `<= 18` e precisou ser corrigido. Teste justamente com 18.

## Checklist

- [ ] par/ímpar testado com 4, 7 e 0
- [ ] maioridade testada com 17, **18** e 19
- [ ] marquei ✅ na tabela do README principal
- [ ] commit e push

## Rodar

```
cd dia-02-par-impar-e-maioridade
java ParOuImpar.java
java MaiorDeIdade.java
```
