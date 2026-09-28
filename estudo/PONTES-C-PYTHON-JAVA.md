# 🌉 Pontes: C → Python → Java

A mesma ideia escrita nas três linguagens. Quando um conceito de Java não fizer sentido, procure aqui como ele fica no C e no Python.

## 1. Olá, mundo

```c
// C
#include <stdio.h>
int main(void) {
    printf("Olá\n");
    return 0;
}
```

```python
# Python
print("Olá")
```

```java
// Java: todo código mora dentro de uma classe
public class Ola {
    public static void main(String[] args) {
        System.out.println("Olá");
    }
}
```

## 2. Ler um número do teclado

```c
int n;
scanf("%d", &n);
```

```python
n = int(input())
```

```java
import java.util.Scanner;   // no topo do arquivo

Scanner sc = new Scanner(System.in);
int n = sc.nextInt();
```

## 3. Divisão

| | C | Python | Java |
|---|---|---|---|
| `7 / 2` | `3` | `3.5` | `3` |
| `7 / 2.0` | `3.5` | `3.5` | `3.5` |
| divisão inteira | `7 / 2` | `7 // 2` | `7 / 2` |

**Java divide igual ao C.**

## 4. Texto

| | C | Python | Java |
|---|---|---|---|
| declarar | `char nome[20] = "Ana";` | `nome = "Ana"` | `String nome = "Ana";` |
| tamanho | `strlen(nome)` | `len(nome)` | `nome.length()` |
| comparar | `strcmp(a, b) == 0` | `a == b` | `a.equals(b)` ⚠️ **nunca** `==` |
| juntar | `strcat` | `a + b` | `a + b` |

## 5. Array

```c
int v[5];
v[10] = 1;          // compila e corrompe a memória em silêncio
```

```python
v = [0] * 5
len(v)
```

```java
int[] v = new int[5];
v.length;           // sem parênteses no array
v[10] = 1;          // para o programa: ArrayIndexOutOfBoundsException
for (int x : v) { } // o "for x in v" do Java
```

## 6. Função

```c
int dobro(int x) { return x * 2; }
```

```python
def dobro(x):
    return x * 2
```

```java
static int dobro(int x) { return x * 2; }   // fica dentro da classe
```

## 7. `struct` → `class`

```c
typedef struct {
    char nome[50];
    double nota;
} Aluno;

Aluno a;
strcpy(a.nome, "Ana");
a.nota = 8.5;
```

```python
class Aluno:
    def __init__(self, nome, nota):
        self.nome = nome
        self.nota = nota

    def aprovado(self):
        return self.nota >= 7

a = Aluno("Ana", 8.5)
```

```java
class Aluno {
    String nome;
    double nota;

    Aluno(String nome, double nota) {   // construtor = __init__
        this.nome = nome;               // this = self
        this.nota = nota;
    }

    boolean aprovado() {
        return nota >= 7;
    }
}

Aluno a = new Aluno("Ana", 8.5);
```

## 8. Ponteiro → referência

```c
Aluno *p = malloc(sizeof(Aluno));
p->nota = 9;
Aluno *q = p;       // q aponta para o MESMO aluno
q->nota = 3;        // p->nota agora também é 3
free(p);
```

```java
Aluno p = new Aluno("Ana", 9);
Aluno q = p;        // q aponta para o MESMO aluno
q.nota = 3;         // p.nota agora também é 3
// não existe free: o garbage collector limpa sozinho
```

- Em Java, **toda variável de objeto é um ponteiro**, só que sem `*` nem `->`.
- `null` é o `NULL`. Usar `null` dá `NullPointerException`, que é o *segmentation fault* que ao menos diz a linha.

## 9. Erros

```c
if (b == 0) return -1;   // e torcer para quem chamou conferir
```

```python
if b == 0:
    raise ValueError("divisão por zero")

try:
    dividir(1, 0)
except ValueError as e:
    print(e)
```

```java
if (b == 0) throw new IllegalArgumentException("divisão por zero");

try {
    dividir(1, 0);
} catch (IllegalArgumentException e) {
    System.out.println(e.getMessage());
}
```

## 10. Lista que cresce

```c
// C: malloc + realloc na mão sempre que encher
```

```python
nomes = []
nomes.append("Ana")
len(nomes); nomes[0]
```

```java
import java.util.*;

List<String> nomes = new ArrayList<>();
nomes.add("Ana");
nomes.size(); nomes.get(0);
```

## 11. Dicionário

```python
idades = {"Ana": 20}
idades["Ana"]
"Ana" in idades
```

```java
Map<String, Integer> idades = new HashMap<>();
idades.put("Ana", 20);
idades.get("Ana");
idades.containsKey("Ana");
```

C não tem dicionário pronto.
