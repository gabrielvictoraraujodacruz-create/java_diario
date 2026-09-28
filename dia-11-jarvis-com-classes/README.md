# Dia 11: Jarvis com classes (POO)

> Original em Python: [`original.py`](original.py) (do meus projetos locais de Python)

## Missão

Refatorar o Jarvis de ontem trocando os mapas por **classes**. Este é o dia mais importante da trilha: Java foi feito para programar orientado a objetos.

## Sugestão de modelo

```java
class Materia {
    String nome;
    List<Double> notas = new ArrayList<>();
    Double notaRecuperacao; // null se não fez

    Materia(String nome) { this.nome = nome; }

    double media() { ... }
    String situacao() { ... }   // APROVADO / REPROVADO
}

class Aluno {
    String nome;
    double frequencia;
    List<Materia> materias = new ArrayList<>();

    boolean reprovadoPorFalta() { ... }
}
```

- `this.nome` é o `self.nome` do Python.
- O construtor tem o **mesmo nome da classe** e é o `__init__` do Java.
- Pode deixar as 3 classes no mesmo arquivo `JarvisPOO.java`. Só a que tem o `main` leva `public`.
- 💡 Repare como `media()` e `situacao()` viram **comportamento da matéria**, em vez de contas soltas no meio do programa.

## Checklist

- [ ] mesmo resultado do dia 10, sem nenhum `Map` de `Map`
- [ ] `Materia` sabe calcular a própria média
- [ ] marquei ✅ na tabela do README principal
- [ ] commit e push

## Rodar

```
cd dia-11-jarvis-com-classes
java JarvisPOO.java
```
