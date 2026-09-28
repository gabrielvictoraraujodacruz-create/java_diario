# 📘 Plano de 30 dias: Java + Git

**30 minutos por dia.** Eu venho do C (que estou estudando na faculdade) e do Python (que uso no estágio), então o plano usa os dois como ponte:
o que é **igual ao C** passa rápido, e o tempo fica para o que é **novo de verdade** no Java, que é a Orientação a Objetos.

## O ritual de cada dia (30 min)

| Tempo | O quê |
|---|---|
| **15 min** | 📺 Assistir as aulas do dia (se passar de 15 min, assistir em 1,5x). Onde tem ⏩ é conteúdo igual ao C, então dá para ver em 2x |
| **10 min** | ⌨️ Digitar o exemplo **sem copiar e colar**, em `estudo/dia-NN/` |
| **5 min** | 📝 Preencher o `ANOTACOES.md` do dia (modelo em [`_modelo/ANOTACOES.md`](_modelo/ANOTACOES.md)) e fazer **commit + push** |

**Regras:**
- O commit é obrigatório, mesmo quando o dia rendeu pouco. É ele que conta no painel.
- Se travar por mais de 10 minutos, pergunte ao Claude, por exemplo *"me dá a ponte do dia 12 em C"* ou *"deu esse erro: ..."*.
- Perdeu um dia? **Não faça dois de uma vez.** Continue de onde parou: a numeração é do estudo, não do calendário.
- Para comparar Java com C e Python lado a lado, use o [**PONTES-C-PYTHON-JAVA.md**](PONTES-C-PYTHON-JAVA.md).
- Dia com 🌿 tem comando novo de Git: anote no [**caderno de Git**](../git/CADERNO-GIT.md).

## Materiais (todos gratuitos, conferidos em 28/09/2026)

| Material | Para quê |
|---|---|
| 📺 [**Maratona Java Virado no Jiraya**](https://www.youtube.com/playlist?list=PL62G310vn6nFIsOCC0H-C2infYgwm8SWW) (DevDojo, William Suane) | **Curso principal.** 284 aulas curtas em português. Os números abaixo são os das aulas dessa playlist. Foi gravado com Java 15 e IntelliJ, mas tudo vale para o Java 21 e o VS Code que eu uso |
| 📺 [Curso de POO Java](https://www.youtube.com/playlist?list=PLHz_AreHm4dkqe2aR0tQK74m8SFe-aGsY) (Curso em Vídeo, Guanabara) | Plano B, para quando um conceito de Orientação a Objetos não entrar de primeira |
| 📺 [Git e GitHub](https://www.cursoemvideo.com/curso/curso-de-git-e-github/) (Curso em Vídeo) | 13 aulas grátis (o certificado é pago), para aprofundar o Git depois |
| 📖 [Pro Git em português](https://git-scm.com/book/pt-br/v2) | O livro oficial do Git, grátis |
| 🎮 [Learn Git Branching](https://learngitbranching.js.org/?locale=pt_BR) | Joguinho no navegador para entender branch e merge, em português |
| 📖 [dev.java/learn](https://dev.java/learn/) | Tutorial oficial do Java (em inglês), para consulta |
| 💪 [MOOC Java da Univ. de Helsinki](https://java-programming.mooc.fi/) | Exercícios extras (em inglês). O curso é antigo e não emite mais certificado, mas o conteúdo continua ótimo |

---

## Semana 1: Git e o básico (quase tudo igual ao C)

### Dia 01 · Git: o primeiro commit feito por mim
- 📖 Pro Git, seções [1.1](https://git-scm.com/book/pt-br/v2/Primeiros-Passos-Sobre-Controle-de-Vers%c3%a3o) e [1.3](https://git-scm.com/book/pt-br/v2/Primeiros-Passos-O-que-%c3%a9-Git%3F) (leitura curta)
- 🌉 Pense no Git como um "salvar com histórico". Cada commit é uma foto do projeto, e dá para voltar em qualquer uma.
- ⌨️ No terminal do VS Code, dentro da pasta `java_diario`:
  ```
  git config --list          # meu nome e e-mail já estão configurados
  git status                 # o que mudou?
  ```
  Abrir o [`git/CADERNO-GIT.md`](../git/CADERNO-GIT.md) e preencher a parte do Dia 01 com as minhas palavras: o que é repositório, commit e push, e o que cada comando faz. Depois:
  ```
  git add .                  # coloca as mudanças no "carrinho" (staging)
  git commit -m "dia 01: primeiro commit feito por mim"   # fecha a compra
  git push                   # manda para o GitHub
  ```
- 🌿 Conferir no GitHub se o quadradinho de hoje ficou verde.

### Dia 02 · Como o Java funciona
- 📺 Maratona **01, 02 e 05** (pule a 03 e a 04, que ensinam a instalar: o JDK 21 já está instalado)
- 🌉 **C:** o `gcc` gera um `.exe` que só roda naquele sistema. **Java:** o `javac` gera um `.class` (bytecode) que roda na **JVM** de qualquer sistema. **Python:** também roda em qualquer lugar, mas só descobre muitos erros na hora de rodar. O Java acha esses erros antes, na compilação.
- ⌨️ `Ola.java`: compilar com `javac Ola.java`, ver o `Ola.class` aparecer e rodar com `java Ola`. Depois rodar direto com `java Ola.java`.
- 🌿 `git log --oneline`: ver a lista de commits. O `.class` não aparece no `git status` porque a `.gitignore` esconde (fica para o dia 04).

### Dia 03 · Tipos primitivos
- 📺 Maratona **09 a 12**
- 🌉 **C:** `int`, `double`, `char` e o cast `(int) x` funcionam do mesmo jeito. O que é novo: existe `boolean` de verdade, e o `int` tem **sempre** 32 bits, em qualquer PC. **Python:** aqui a variável tem tipo fixo, então `int x = 5; x = "oi";` nem compila.
- ⌨️ `Tipos.java`: declarar uma variável de cada tipo, imprimir, e testar `(int) 9.99`.
- 🌿 Rodar `git diff` antes do `add` para ver exatamente o que mudou.

### Dia 04 · Strings
- 📺 Maratona **13 e 14**
- 🌉 **C:** `char nome[20]` e `strcmp`. **Java:** `String` é um objeto, e o tamanho sai de `nome.length()`. ⚠️ Comparar texto é com `a.equals(b)`, **nunca** com `==`. **Python:** a String também é imutável, como no Python.
- ⌨️ `Textos.java`: testar `==` e `equals` com texto digitado pelo usuário e ver a diferença.
- 🌿 Abrir o `.gitignore` da raiz e entender o que cada linha esconde do Git.

### Dia 05 · Operadores ⏩
- 📺 Maratona **15 a 19** (em 2x: é igual ao C)
- 🌉 Diferenças: `+` também junta texto; `&&` e `||` só aceitam `boolean` (no C, qualquer `int` serve). `7 / 2` dá `3`, igual ao C e **diferente do Python**.
- ⌨️ `Operadores.java`: imprimir `7/2`, `7/2.0`, `7%2`, `"a"+1+2` e `1+2+"a"`, e explicar os resultados nas anotações.
- 🌿 Mensagem de commit boa é curta e diz o que foi feito: `dia 05: operadores e divisão inteira`.

### Dia 06 · Condicionais ⏩
- 📺 Maratona **20, 21, 22 e 25** (a 23, a 24 e a 26 são opcionais)
- 🌉 `if/else` e o ternário `x > 0 ? "pos" : "neg"` são iguais ao C. Novo: o `switch` moderno, que não precisa de `break`:
  ```java
  String dia = switch (n) { case 1 -> "domingo"; case 2 -> "segunda"; default -> "?"; };
  ```
- ⌨️ `Condicionais.java`: nota → conceito (A/B/C/D) primeiro com `if` e depois com `switch`.
- 🌿 Estragar um arquivo de propósito e desfazer com `git restore NomeDoArquivo.java`.

### Dia 07 · Revisão + ler do teclado
- 📺 Maratona **68** (leitura de dados pelo console)
- 🌉 **C:** `scanf("%d", &n)`. **Python:** `int(input())`. **Java:** `Scanner`. ⚠️ No meu PC, `nextDouble()` espera **vírgula**: `1,75` funciona e `1.75` dá erro.
- ⌨️ `Imc.java`: ler peso e altura, calcular o IMC e classificar. Isso junta a semana inteira.
- 🎮 Learn Git Branching: fase **Introdução**, níveis 1 e 2 (commit e branch).

---

## Semana 2: Laços, arrays e as primeiras classes

### Dia 08 · Laços ⏩
- 📺 Maratona **27 a 31** (em 2x: `for`, `while`, `do while`, `break` e `continue` são iguais ao C)
- ⌨️ `Lacos.java`: tabuada com `for`, e somar números até digitar 0 com `do while`.
- 🌿 `git log --oneline --graph`

### Dia 09 · Arrays
- 📺 Maratona **32 a 35**
- 🌉 **C:** `int v[5];` e ler `v[10]` devolve lixo em silêncio. **Java:** `int[] v = new int[5];`, o tamanho vem de `v.length`, e ler `v[10]` **para o programa** com `ArrayIndexOutOfBoundsException`. **Python:** o array tem tamanho fixo, então não é a `list`. O `for (int x : v)` é o `for x in v`.
- ⌨️ `Notas.java`: ler 5 notas num array e mostrar a média e a maior nota.
- 🌿 `git show`: ver o conteúdo do último commit.

### Dia 10 · Matrizes
- 📺 Maratona **36 a 38**
- 🌉 **C:** `int m[3][3]`. **Java:** `int[][] m = new int[3][3];`
- ⌨️ `Velha.java`: montar e imprimir um tabuleiro de jogo da velha.

### Dia 11 · Classes: o `struct` que ganhou funções
- 📺 Maratona **39 a 41**
- 🌉 **C:** `struct Aluno { char nome[50]; double nota; };`. **Python:** `class Aluno:`. Em Java, a classe junta os **dados** (como o struct) e as **ações** (métodos). Veja a ponte 7 no arquivo de pontes.
- ⌨️ `Aluno.java` com nome e nota, e um `main` que cria 2 alunos com `new`.
- ⚠️ Se colocar duas classes no mesmo arquivo, **a que tem o `main` vem primeiro**. Senão o `java Arquivo.java` responde `can't find main(String[]) method`.

### Dia 12 · Referência de objetos: o ponteiro disfarçado
- 📺 Maratona **42 e 43**
- 🌉 **C:** `Aluno *q = p;` copia o **endereço**, não o aluno. Em Java, `Aluno q = p;` faz **exatamente isso**: toda variável de objeto é um ponteiro, só que sem `*` nem `->`. `null` é o `NULL` do C, e usar `null` dá `NullPointerException`, que é um "segmentation fault" que ao menos diz a linha. **Python:** funciona igual (`b = a` numa lista).
- ⌨️ Provar que, depois de `q = p`, mudar `q.nota` muda `p.nota`.

### Dia 13 · Métodos
- 📺 Maratona **44 a 47**
- 🌉 Método é a função do C (e o `def` do Python), só que mora dentro da classe.
- ⌨️ Adicionar os métodos `boolean aprovado()` e `void imprimir()` na classe `Aluno`.

### Dia 14 · Revisão + primeira branch
- 🎮 Learn Git Branching: **Introdução**, níveis 3 e 4 (merge e rebase)
- ⌨️ Na prática:
  ```
  git switch -c revisao-semana2   # cria uma branch e entra nela
  # exercício: classe Produto (nome, preço) + array de 3 produtos + total da compra
  git add . && git commit -m "dia 14: revisão com classe Produto"
  git switch main
  git merge revisao-semana2       # traz o trabalho para a main
  git push
  ```

---

## Semana 3: Orientação a Objetos de verdade

### Dia 15 · Parâmetros e o `this`
- 📺 Maratona **48 a 51**
- 🌉 **C:** o parâmetro é cópia, e para alterar o original é preciso passar ponteiro. **Java:** tipo primitivo vai como **cópia** e objeto vai como **referência**, automaticamente. `this` é o `self` do Python.
- ⌨️ Um método que tenta mudar um `int` (não muda) e outro que muda um `Aluno` (muda).

### Dia 16 · Encapsulamento: `private`, get e set
- 📺 Maratona **54 a 56**
- 🌉 **Python:** `_saldo` é só uma convenção. **Java:** com `private`, ninguém de fora mexe, e o compilador impede.
- ⌨️ `Conta.java`: saldo `private`, com `depositar()` e `sacar()` que não deixam o saldo ficar negativo.

### Dia 17 · Sobrecarga e construtores
- 📺 Maratona **57 a 59**
- 🌉 O construtor é o `__init__` do Python. Sobrecarga é ter vários métodos com o mesmo nome e parâmetros diferentes, algo que nem o C nem o Python têm.
- ⌨️ Dar à `Conta` dois construtores: `Conta(titular)` e `Conta(titular, saldoInicial)`.

### Dia 18 · `static`
- 📺 Maratona **61 e 62**
- 🌉 Aqui você finalmente entende o `public static void main`. Um atributo `static` é compartilhado por todos os objetos, como uma "variável global" da classe.
- ⌨️ Um contador `static` de quantas contas já foram criadas.

### Dia 19 · Associação (liga com MBD!)
- 📺 Maratona **64 a 66**
- 🌉 É o **relacionamento 1:N do MER** de Modelagem de Banco de Dados, só que em código: uma `Turma` **tem vários** `Aluno`.
- ⌨️ `Turma.java` com um array de `Aluno` e um método `media()` da turma.

### Dia 20 · Herança
- 📺 Maratona **71 a 74**
- 🌉 **Python:** `class Aluno(Pessoa)` e `super().__init__()`. **Java:** `class Aluno extends Pessoa` e `super(...)`.
- ⌨️ `Pessoa`, e a partir dela `Aluno` e `Professor`.

### Dia 21 · Revisão + Pull Request
- 📺 Maratona **76** (`toString`, o `__str__` do Java)
- ⌨️ Adicionar `toString()` em `Pessoa`, `Aluno` e `Professor`.
- 🌿 O fluxo de quem trabalha em equipe:
  ```
  git switch -c dia-21
  # ... código ...
  git add . && git commit -m "dia 21: toString"
  git push -u origin dia-21
  ```
  No GitHub, abrir um **Pull Request** da `dia-21` para a `main` e dar merge pelo site. Depois, no PC:
  ```
  git switch main
  git pull              # traz para o PC o que mudou no GitHub
  ```

---

## Semana 4: Abstração, erros e coleções

### Dia 22 · Classes abstratas
- 📺 Maratona **84 e 85**
- ⌨️ Uma `Forma` abstrata com `area()`, e as classes `Circulo` e `Retangulo` que herdam dela.

### Dia 23 · Interfaces
- 📺 Maratona **87 e 88**
- 🌉 Interface é um **contrato**: quem assina é obrigado a ter aqueles métodos. **Python:** é parecido com o *duck typing*, só que verificado pelo compilador.
- ⌨️ Uma interface `Pagavel` com `double valorAPagar()`, usada em `Boleto` e `Salario`.

### Dia 24 · Polimorfismo
- 📺 Maratona **90 a 92**
- ⌨️ Um array `Forma[]` com círculos e retângulos misturados, e um laço que soma todas as áreas sem saber quem é quem.

### Dia 25 · Exceções, parte 1
- 📺 Maratona **95 a 98**
- 🌉 **C:** `return -1` e torcer para quem chamou conferir. **Python:** `raise` e `try/except`. **Java:** `throw` e `try/catch`.
- ⌨️ `Conta.sacar()` lança `IllegalArgumentException` quando o saldo não dá, e o `main` trata.

### Dia 26 · Exceções, parte 2
- 📺 Maratona **99, 100 e 103**
- 🌉 Novo no Java: exceção **checked**, que o compilador **obriga** a tratar. *try-with-resources* é o `with open(...)` do Python.
- ⌨️ Ler um arquivo `.txt` linha por linha com try-with-resources.

### Dia 27 · Wrappers e StringBuilder
- 📺 Maratona **106, 107 e 111**
- 🌉 `int` é primitivo e `Integer` é objeto (no Python, tudo é objeto). `Integer.parseInt("42")` é o `int("42")`. `StringBuilder` monta texto grande sem desperdício, como o `"".join()`.
- ⌨️ Converter texto em número tratando o erro, e montar uma tabela com `StringBuilder`.

### Dia 28 · `ArrayList`: a `list` do Java
- 📺 Maratona **166 a 168**
- 🌉 **C:** lista que cresce exige `realloc` na mão. **Python:** `list`. **Java:** `ArrayList`.
- ⌨️ Lista de tarefas com adicionar, remover e listar.

### Dia 29 · `HashMap`: o `dict` do Java
- 📺 Maratona **178 e 179**
- 🌉 **Python:** `dict`. **C:** não tem pronto.
- ⌨️ Contar quantas vezes cada palavra aparece numa frase.

### Dia 30 · Revisão final + tag
- ⌨️ Mini-projeto **Agenda**: classe `Contato`, um `ArrayList<Contato>` e um menu com `Scanner` (adicionar, listar, buscar, remover).
- 📝 Escrever `estudo/RETROSPECTIVA.md`: o que ficou fácil, o que ainda está difícil e o que foi mais diferente do C.
- 🌿 Marcar o fim da fase:
  ```
  git tag fase-1-concluida
  git push --tags
  ```
- 🏁 **Próximo passo:** a [Fase 2 (prática)](../pratica), refazendo meus projetos de Python em Java.
