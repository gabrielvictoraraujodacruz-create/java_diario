# Script de consulta de CEP usando a API pública do ViaCEP.
# Objetivo: receber um CEP, buscar os dados na API, imprimir o JSON
# formatado e tratar todos os erros possíveis sem que o script quebre.

import json                  # Para formatar/parsear a resposta JSON da API
import re                    # Para limpar o CEP digitado (remover hífens, espaços, etc.)
import urllib.error          # Tipos de erro de rede/HTTP do urllib
import urllib.request        # Cliente HTTP nativo do Python (sem precisar instalar nada)


def consultar_cep(cep: str) -> dict | None:
    """
    Consulta um CEP na API ViaCEP e retorna os dados como dicionário.
    Retorna None em caso de erro (CEP inválido, sem conexão, etc.).
    """

    # 1) Sanitiza a entrada: remove tudo que não for dígito.
    #    Assim "01001-000", "01001 000" ou "01001000" viram "01001000".
    cep_limpo = re.sub(r"\D", "", cep or "")

    # 2) Validação local antes de bater na API: economiza requisição
    #    e devolve mensagem clara se o usuário digitou algo errado.
    if len(cep_limpo) != 8:
        print(f"CEP inválido: '{cep}'. Informe 8 dígitos (ex.: 01001-000).")
        return None

    # 3) Monta a URL no formato esperado pelo ViaCEP.
    url = f"https://viacep.com.br/ws/{cep_limpo}/json/"

    # 4) Bloco try/except cobrindo todas as falhas possíveis da requisição.
    try:
        # timeout=10 evita que o script trave caso a API esteja lenta/fora do ar.
        with urllib.request.urlopen(url, timeout=10) as resposta:
            # Lê os bytes, decodifica em UTF-8 e converte de JSON para dict.
            dados = json.loads(resposta.read().decode("utf-8"))

        # 5) O ViaCEP retorna {"erro": true} quando o CEP tem formato válido
        #    mas não existe na base. Tratamos esse caso como "não encontrado".
        if dados.get("erro"):
            print(f"CEP {cep_limpo} não encontrado na base do ViaCEP.")
            return None

        # Se chegou até aqui, deu tudo certo — devolve o dicionário.
        return dados

    # 6) Erros HTTP (status 4xx/5xx vindos do servidor do ViaCEP).
    except urllib.error.HTTPError as e:
        print(f"Erro HTTP ao consultar o CEP ({e.code}): {e.reason}")

    # 7) Falhas de rede em geral: DNS, sem internet, host inacessível, etc.
    except urllib.error.URLError as e:
        print(f"Erro de conexão ao acessar o ViaCEP: {e.reason}")

    # 8) Caso o servidor demore mais que o timeout definido acima.
    except TimeoutError:
        print("Tempo de conexão esgotado ao consultar o ViaCEP.")

    # 9) Se a resposta vier corrompida e não puder ser convertida em JSON.
    except json.JSONDecodeError:
        print("Resposta inválida do ViaCEP (não é um JSON válido).")

    # 10) Rede de segurança final: qualquer outro erro inesperado é capturado
    #     aqui para que o programa NUNCA quebre, apenas registre e siga.
    except Exception as e:
        print(f"Erro inesperado: {e}")

    # Em qualquer um dos except acima, retornamos None para sinalizar falha.
    return None


def imprimir_resultado(dados: dict) -> None:
    """Imprime o JSON formatado e um resumo legível dos campos principais."""

    # JSON identado em 4 espaços e com acentuação preservada (ensure_ascii=False).
    print("\n--- JSON recebido ---")
    print(json.dumps(dados, indent=4, ensure_ascii=False))

    # Resumo "humano" dos campos mais usados — usa .get() para não quebrar
    # caso algum campo opcional não venha preenchido na resposta.
    print("\n--- Resumo ---")
    print(f"CEP.........: {dados.get('cep', '')}")
    print(f"Logradouro..: {dados.get('logradouro', '')}")
    print(f"Bairro......: {dados.get('bairro', '')}")
    print(f"Cidade/UF...: {dados.get('localidade', '')}/{dados.get('uf', '')}")
    print(f"DDD.........: {dados.get('ddd', '')}")


# Ponto de entrada do script: só executa quando rodado diretamente
# (e não quando o arquivo é importado como módulo por outro script).
if __name__ == "__main__":
    try:
        # input() pode falhar se o usuário cancelar (Ctrl+C) ou se a entrada
        # padrão for fechada (Ctrl+D / EOF) — tratamos os dois casos.
        cep_informado = input("Digite o CEP: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nOperação cancelada pelo usuário.")
        raise SystemExit(0)

    # Faz a consulta e, se houver retorno válido, imprime os dados.
    resultado = consultar_cep(cep_informado)
    if resultado:
        imprimir_resultado(resultado)
