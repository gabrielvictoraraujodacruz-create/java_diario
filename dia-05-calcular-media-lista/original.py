# Atividade 4: a versão em Python que saiu do "prompt mestre".

def calcular_media(lista_numeros):
    """
    Calcula a média de uma lista de números.
    Parâmetros:
        lista_numeros (list): Lista contendo números
    Retorna:
        float: Média dos números
    Levanta:
        ValueError: Se a lista estiver vazia ou contiver valores inválidos
    """
    # Verifica se a lista está vazia
    if not lista_numeros:
        raise ValueError("A lista não pode estar vazia.")
    # Verifica se todos os elementos são números
    for item in lista_numeros:
        if not isinstance(item, (int, float)):
            raise ValueError("Todos os elementos devem ser números.")
    # Soma os elementos da lista
    soma = sum(lista_numeros)
    # Calcula a média
    media = soma / len(lista_numeros)
    return media


# Casos de teste
# Caso 1: Lista normal
print(calcular_media([10, 20, 30]))  # Esperado: 20.0
# Caso 2: Lista com um número
print(calcular_media([5]))  # Esperado: 5.0
# Caso 3: Lista vazia (erro)
try:
    print(calcular_media([]))  # Esperado: erro
except ValueError as erro:
    print(f"Erro: {erro}")
