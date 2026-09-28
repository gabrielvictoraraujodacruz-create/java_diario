# Projeto 04: Média das notas

> Original em Python: [`original.py`](original.py) (do repo [programacoes_de_computadores](https://github.com/gabrielvictoraraujodacruz-create/programacoes_de_computadores))

## Missão

Ler duas notas, calcular a média e dizer: Aprovado (≥ 7), Recuperação (≥ 5 e < 7) ou Reprovado (< 5).

## O que muda no Java

⚠️ **A pegadinha mais comum de quem vem do Python.** No Python, `/` sempre dá número quebrado. No Java, **inteiro dividido por inteiro dá inteiro**:

```java
int a = 7, b = 8;
System.out.println((a + b) / 2);    // 7   (cortou o .5!)
System.out.println((a + b) / 2.0);  // 7.5
```

Faça o programa com `double` e depois teste trocando para `int`, só para ver a média sair errada.

| Python | Java |
|---|---|
| `elif` | `else if` |
| `and` / `or` / `not` | `&&` / `\|\|` / `!` |

## Checklist

- [ ] notas 7 e 8 mostram média 7.5
- [ ] testei os três resultados (aprovado, recuperação, reprovado)
- [ ] marquei ✅ na tabela da Fase 2 no README principal
- [ ] commit e push

## Rodar

```
cd pratica/projeto-04-media-das-notas
java MediaDasNotas.java
```
