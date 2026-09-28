# Projeto 08: Sistema de notificação

> Original em Python: [`original.py`](original.py) (do repo [engenharia_de_prompt_aplicacoes_ai](https://github.com/gabrielvictoraraujodacruz-create/engenharia_de_prompt_aplicacoes_ai))

## Missão

Recriar as 4 funções (`verificarCondicao`, `dispararAlertaConsole`, `dispararAlertaEmail` e `monitorarSistema`) e o exemplo de uso.

## O que muda no Java

- Método que não devolve nada tem o tipo `void`: `static void dispararAlertaConsole(String mensagem)`.
- ⚠️ Java **não tem parâmetro com valor padrão** (`destinatario="admin@sistema.com"`). A saída é a **sobrecarga**: dois métodos com o mesmo nome e parâmetros diferentes.

```java
static void dispararAlertaEmail(String mensagem) {
    dispararAlertaEmail(mensagem, "admin@sistema.com");
}

static void dispararAlertaEmail(String mensagem, String destinatario) {
    // envio de verdade (simulado)
}
```

- Para montar texto com variáveis, dá para usar `String.format("Valor = %d, Limite = %d", valor, limite)`.

## Checklist

- [ ] um valor abaixo do limite imprime "dentro dos limites"
- [ ] um valor acima dispara os dois alertas
- [ ] marquei ✅ na tabela da Fase 2 no README principal
- [ ] commit e push

## Rodar

```
cd pratica/projeto-08-sistema-notificacao
java SistemaNotificacao.java
```
