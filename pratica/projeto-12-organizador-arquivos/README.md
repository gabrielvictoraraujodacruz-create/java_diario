# Projeto 12: Organizador de arquivos

> Original em Python: [`original.py`](original.py) (do repo [engenharia_de_prompt_aplicacoes_ai](https://github.com/gabrielvictoraraujodacruz-create/engenharia_de_prompt_aplicacoes_ai))

## Missão

Mover os arquivos de uma pasta para subpastas com o nome da extensão (`pdf/`, `jpg/`, `_sem_extensao/`).

## O que muda no Java

```java
import java.nio.file.*;

Path pasta = Path.of(args[0]);          // pasta vem pela linha de comando
try (var itens = Files.list(pasta)) {
    for (Path arquivo : itens.toList()) {
        if (Files.isDirectory(arquivo)) continue;
        String nome = arquivo.getFileName().toString();
        // achar a extensão com nome.lastIndexOf('.')
        Files.createDirectories(destino);
        Files.move(arquivo, destino.resolve(nome));
    }
}
```

- ⚠️ Em Java, operação de arquivo **obriga** a tratar `IOException` (é uma *checked exception*). O código nem compila sem `try/catch` ou sem `throws IOException` no método.
- Rodar passando a pasta: `java OrganizadorArquivos.java teste`

⚠️ **Não teste na sua pasta Downloads de verdade.** Crie uma pasta `teste/` aqui dentro com uns arquivos falsos (`a.txt`, `b.pdf`, `c`). A `.gitignore` já ignora a pasta `teste/`.

## Checklist

- [ ] arquivos separados por extensão
- [ ] arquivo sem extensão foi para `_sem_extensao/`
- [ ] pasta inexistente mostra aviso, sem estourar erro
- [ ] marquei ✅ na tabela da Fase 2 no README principal
- [ ] commit e push

## Rodar

```
cd pratica/projeto-12-organizador-arquivos
java OrganizadorArquivos.java
```
