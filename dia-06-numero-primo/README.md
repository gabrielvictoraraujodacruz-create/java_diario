# Dia 06: Número primo

> Original em Python: [`original.py`](original.py) (do repo [engenharia_de_prompt_aplicacoes_ai](https://github.com/gabrielvictoraraujodacruz-create/engenharia_de_prompt_aplicacoes_ai))

## Missão

Recriar o `is_prime` (a versão refatorada, que pula os pares) como o método `ehPrimo(int n)`.

## O que muda no Java

- O `for` clássico tem 3 partes, que são início, condição e passo:

```java
for (int i = 3; i <= limite; i += 2) { ... }
```

Esse é o `range(3, limite + 1, 2)` do Python.

- Raiz quadrada: `(int) Math.sqrt(n)`. O `(int)` na frente é um *cast*, que converte o `double` em `int`.
- 💡 O "código original" desse notebook tinha o `for` indentado por engano **depois** do `return`, então ele nunca rodava. Em Java as chaves deixam esse tipo de erro bem mais visível, e o compilador ainda acusa *unreachable statement*.

## Checklist

- [ ] testei 0, 1, 2, 9, 17 e 97
- [ ] o `main` imprime os primos de 1 a 50
- [ ] marquei ✅ na tabela do README principal
- [ ] commit e push

## Rodar

```
cd dia-06-numero-primo
java NumeroPrimo.java
```
