# 🌿 Meu caderno de Git

Minha "cola" de Git, escrita com as minhas palavras. Cada dia do plano que tem 🌿 acrescenta um comando aqui.

> Os comandos rodam no **Git Bash**, sempre **dentro da pasta do repositório**, porque é ela que o Git conhece e que está ligada ao GitHub.

## Dia 01: o básico

**Repositório é:** onde guardamos os dados

**Commit é:** Commit é quando atualizamos o repositório

**Push é:** É enviar atualizações salvas no repositório local

**Os 3 lugares por onde uma mudança passa:** Ele passa por modificado, preparado e depois commit

| Comando | O que faz |
|---|---|
| `git config --list` | mostra as configuraçoes do Git (exemplo: nome, email que vao assinados no commit); |
| `git status` | o que mudou, o que está no carrinho e se o PC está igual ao GitHub |
| `git add .` | coloca todas as mundaças da pasta atual no carrinho(Esta preparado) |
| `git commit -m "..."` | tira a foto do que está no carrinho, com a mensagem entre aspas (Ele tira foto do que esta alterando) |
| `git push` | Manda as fotos para o Github (atualiza) |

## 🧭 Andar pelas pastas no Git Bash

| Comando | O que faz |
|---|---|
| `pwd` | mostra **onde estou** agora |
| `ls` | lista o que tem na pasta atual (`ls -a` mostra também os escondidos, como o `.git`) |
| `cd nome-da-pasta` | entra numa pasta que está aqui dentro |
| `cd ..` | volta uma pasta (sobe um nível) |
| `cd ~` | volta para a minha pasta de usuário |
| `cd /e/` | vai para o disco E: (no Git Bash os discos são `/c/`, `/e/`...) |
| `mkdir nome` | cria uma pasta nova |
| `explorer .` | abre a pasta atual no Explorador de Arquivos |

**Atalhos que poupam digitação:**
- **TAB completa o nome:** digite `cd /e/ACA` e aperte TAB, que ele completa `ACADEMICO GABRIEL`.
- **Setinha ↑** traz de volta os comandos que eu já digitei.
- **Botão direito dentro de uma pasta no Explorador → "Open Git Bash here"** abre o Git Bash **já dentro daquela pasta**, sem precisar do `cd`.
- **Nome com espaço vai entre aspas:** `cd "/e/ACADEMICO GABRIEL"`.

## 🧪 Exercício: criar um repositório do zero e mandar para o GitHub

**1. Criar a pasta de teste e entrar nela:**
```
cd "/e/ACADEMICO GABRIEL/PROJETOS"
mkdir teste-git
cd teste-git
```

**2. Criar um arquivo:**
```
echo "# Meu teste de Git" > README.md
ls
```

**3. Virar repositório e fazer o primeiro commit:**
```
git init
git add .
git commit -m "primeiro commit"
git branch -M main
```
(`git init` cria a pasta escondida `.git`; `git branch -M main` troca o nome da branch de `master` para `main`, que é o nome que o GitHub usa)

**4. No site do GitHub:** **+** → **New repository** → nome `teste-git` → **Private** → **não** marcar "Add a README" → **Create repository**.

**5. Ligar ao GitHub e enviar:**
```
git remote add origin https://github.com/gabrielvictoraraujodacruz-create/teste-git.git
git push -u origin main
```
(`origin` é o apelido do endereço do GitHub; o `-u` só é preciso na primeira vez, depois é só `git push`)

**6. Conferir:** abrir `github.com/gabrielvictoraraujodacruz-create/teste-git`, onde o README tem que aparecer.

**Atalho** que faz os passos 4 e 5 de uma vez:
```
gh repo create teste-git --private --source=. --push
```

**Para apagar o teste depois:** no GitHub, no repositório → **Settings** → lá no fim, **Delete this repository**. No PC, é só apagar a pasta `teste-git`.

⚠️ **Cuidados:** nunca fazer isso em pasta com dado de cliente; não fazer `git init` em pasta gigante (C:\, pasta de usuário); não criar repositório dentro de outro (se o Git Bash já mostra `(main)`, eu já estou dentro de um).

## Comandos dos próximos dias

| Dia | Comando | O que faz |
|---|---|---|
| 02 | `git log --oneline` | |
| 03 | `git diff` | |
| 04 | `.gitignore` | |
| 05 | mensagem de commit boa | |
| 06 | `git restore arquivo` | |
| 08 | `git log --oneline --graph` | |
| 09 | `git show` | |
| 14 | `git switch -c nome` | |
| 14 | `git merge nome` | |
| 21 | `git push -u origin nome` | |
| 21 | Pull Request | |
| 21 | `git pull` | |
| 30 | `git tag` | |
