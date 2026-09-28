# Dia 05: Média de uma lista

> Original em Python: [`original.py`](original.py) (do repo [engenharia_de_prompt_aplicacoes_ai](https://github.com/gabrielvictoraraujodacruz-create/engenharia_de_prompt_aplicacoes_ai))

## Missão

Recriar a função `calcular_media` como um método Java, com os mesmos 3 casos de teste do original.

## O que muda no Java

- Lista de tamanho fixo é um **array**:

```java
double[] numeros = {10, 20, 30};
numeros.length          // tamanho (sem parênteses!)
for (double n : numeros) { ... }   // o "for item in lista" do Java
```

- A função vira um método `static` fora do `main`:

```java
static double calcularMedia(double[] numeros) { ... }
```

- Para lançar erro: `throw new IllegalArgumentException("A lista não pode estar vazia.");`
- Para tratar:

```java
try {
    calcularMedia(new double[] {});
} catch (IllegalArgumentException e) {
    System.out.println("Erro: " + e.getMessage());
}
```

- 💡 O original confere se "todos os elementos são números". Em Java **isso não precisa**, porque um `double[]` só aceita números. O compilador já faz essa checagem por você. É uma das grandes vantagens da tipagem estática.

## Checklist

- [ ] `[10, 20, 30]` dá 20.0
- [ ] `[5]` dá 5.0
- [ ] a lista vazia mostra a mensagem de erro, sem quebrar o programa
- [ ] marquei ✅ na tabela do README principal
- [ ] commit e push

## Rodar

```
cd dia-05-calcular-media-lista
java CalcularMedia.java
```
