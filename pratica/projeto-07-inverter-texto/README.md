# Projeto 07: Inverter texto

> Original em Python: [`original.py`](original.py) (do repo [engenharia_de_prompt_aplicacoes_ai](https://github.com/gabrielvictoraraujodacruz-create/engenharia_de_prompt_aplicacoes_ai))

## Missão

Fazer as duas versões do original:

1. `inverteManual(String texto)`, com laço letra por letra;
2. `inverte(String texto)`, usando `StringBuilder`.

## O que muda no Java

| Python | Java |
|---|---|
| `len(texto)` | `texto.length()` (com parênteses, ao contrário do array) |
| `texto[i]` | `texto.charAt(i)` |
| `texto[::-1]` | `new StringBuilder(texto).reverse().toString()` |

⚠️ **Pegadinha clássica:** em Java, `==` **não compara o conteúdo** de Strings. Ele compara se são o mesmo objeto na memória. Use sempre:

```java
palavra.equals(outra)
palavra.equalsIgnoreCase(outra)   // ignora maiúscula/minúscula
```

## Desafio extra (opcional)

Método `ehPalindromo(String texto)`: "Arara" deve dar `true`.

## Checklist

- [ ] as duas versões devolvem "LEIRBAG" para "GABRIEL"
- [ ] marquei ✅ na tabela da Fase 2 no README principal
- [ ] commit e push

## Rodar

```
cd pratica/projeto-07-inverter-texto
java InverterTexto.java
```
