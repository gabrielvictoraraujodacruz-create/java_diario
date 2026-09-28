#codigo original:

def inverte_texto(texto):
    invertido = ''
    for letra in texto:
        invertido = letra + invertido
    return invertido

print(f'nome invertido: {inverte_texto("GABRIEL")}')

#codigo refatorado com comentarios:

def inverte_texto(texto: str) -> str:
    """
    Recebe uma string e retorna ela invertida.

    Parâmetros:
        texto (str): A string que será invertida.

    Retorna:
        str: A string com os caracteres na ordem inversa.
    """
    # Forma mais simples e eficiente em Python: fatiamento com passo -1.
    # [::-1] significa "percorra a string do fim para o começo".
    return texto[::-1]


def inverte_texto_manual(texto: str) -> str:
    """
    Versão alternativa que inverte o texto manualmente,
    útil para fins didáticos (mostra a lógica passo a passo).
    """
    invertido = ''  # Acumulador que vai guardar o resultado final

    # Percorre cada letra da string original
    for letra in texto:
        # Coloca a letra atual ANTES do que já foi acumulado.
        # Assim, a última letra adicionada fica sempre no início.
        invertido = letra + invertido

    return invertido


# Bloco principal: só executa quando o arquivo é rodado diretamente
if __name__ == '__main__':
    nome = 'GABRIEL'
    print(f'Nome invertido (versão Pythonica): {inverte_texto(nome)}')
    print(f'Nome invertido (versão manual):    {inverte_texto_manual(nome)}')
