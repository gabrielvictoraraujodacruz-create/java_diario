# Projeto 13: Consulta de CEP (API)

> Original em Python: [`original.py`](original.py) (do repo [engenharia_de_prompt_aplicacoes_ai](https://github.com/gabrielvictoraraujodacruz-create/engenharia_de_prompt_aplicacoes_ai))

## Missão

Pedir um CEP, limpar, validar os 8 dígitos, consultar o ViaCEP e mostrar o resultado.

## O que muda no Java

```java
import java.net.URI;
import java.net.http.*;

String cepLimpo = cep.replaceAll("\\D", "");   // mesmo re.sub(r"\D", "", cep)

HttpClient cliente = HttpClient.newHttpClient();
HttpRequest req = HttpRequest.newBuilder(
        URI.create("https://viacep.com.br/ws/" + cepLimpo + "/json/")).build();
HttpResponse<String> resp = cliente.send(req, HttpResponse.BodyHandlers.ofString());

resp.statusCode();  // 200?
resp.body();        // o JSON como texto
```

- O Java puro **não tem leitor de JSON** embutido (no Python é o `import json`). Por enquanto, imprima o `body()` inteiro. Se der vontade, tente tirar só o campo `"logradouro"` com `indexOf` e `substring`. Mais para frente dá para usar a biblioteca Gson.
- O ViaCEP devolve `{"erro": "true"}` para CEP que não existe. Trate esse caso.

## Checklist

- [ ] `70040-020` e `70040020` funcionam
- [ ] `123` diz "CEP inválido" sem consultar a API
- [ ] `99999999` diz "CEP não encontrado"
- [ ] marquei ✅ na tabela da Fase 2 no README principal
- [ ] commit e push

## Rodar

```
cd pratica/projeto-13-consulta-cep
java ConsultaCep.java
```
