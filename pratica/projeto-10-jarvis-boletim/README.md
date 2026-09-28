# Projeto 10: Jarvis: boletim do aluno

> Original em Python: [`original.py`](original.py) (dos meus projetos locais de Python)

## Missão

Traduzir o Jarvis do jeito que ele está (cadastro, notas por bimestre, recuperação e consulta), usando as coleções do Java no lugar dos dicionários.

## O que muda no Java

| Python | Java |
|---|---|
| `lista = []` | `List<Double> lista = new ArrayList<>();` |
| `lista.append(x)` | `lista.add(x)` |
| `['Portugues', 'Matematica']` | `List.of("Portugues", "Matematica")` |
| `d = {}` | `Map<String, Double> d = new HashMap<>();` |
| `d[chave] = valor` | `d.put(chave, valor)` |
| `chave in d` | `d.containsKey(chave)` |
| `for k, v in d.items():` | `for (var item : d.entrySet()) { item.getKey(); item.getValue(); }` |

Imports: `import java.util.*;`

🐛 **Bug no original para corrigir na versão Java:** a linha `if freq < faltas_permitidas` compara a **frequência** com as **faltas permitidas** (300). Pelos critérios lá em cima, o certo é comparar com `frequencia_minima` (900).

💡 Você vai sentir que dicionário dentro de dicionário fica feio em Java (`Map<String, Map<String, Object>>`). **É de propósito.** No projeto 11 isso vira classe.

## Checklist

- [ ] cadastro e consulta funcionando
- [ ] frequência 500 reprova por falta e 950 passa
- [ ] marquei ✅ na tabela da Fase 2 no README principal
- [ ] commit e push

## Rodar

```
cd pratica/projeto-10-jarvis-boletim
java Jarvis.java
```
