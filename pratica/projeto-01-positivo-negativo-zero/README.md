# Projeto 01: Positivo, negativo ou zero

> Original em Python: [`original.py`](original.py) (do repo [programacoes_de_computadores](https://github.com/gabrielvictoraraujodacruz-create/programacoes_de_computadores))

## Missão

Ler um número inteiro e dizer se ele é positivo, negativo ou zero.

## O que muda no Java

Todo código fica dentro de uma **classe**, e o programa começa pelo método `main`:

```java
public class PositivoNegativoZero {
    public static void main(String[] args) {
        // o programa começa aqui
    }
}
```

- O nome da classe tem que ser **igual ao nome do arquivo**.
- Toda variável tem o tipo declarado: `int numero = 10;`
- Toda instrução termina com `;`.
- Quem marca os blocos são as chaves `{ }`. A indentação serve só para leitura.

| Python | Java |
|---|---|
| `input("texto")` | `Scanner sc = new Scanner(System.in);` e depois `sc.nextInt()`. Precisa de `import java.util.Scanner;` no topo do arquivo |
| `print(f"O número é {x}")` | `System.out.println("O número é " + x);` |
| `elif` | `else if` |
| `if numero > 0:` | `if (numero > 0) { ... }`, com a condição sempre entre parênteses |

## Checklist

- [ ] roda com `java PositivoNegativoZero.java`
- [ ] testei com 5, -3 e 0
- [ ] marquei ✅ na tabela da Fase 2 no README principal
- [ ] commit e push

## Rodar

```
cd pratica/projeto-01-positivo-negativo-zero
java PositivoNegativoZero.java
```
