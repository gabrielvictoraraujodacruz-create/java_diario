#codigo original

def is_prime(n: int) -> bool:
    if n <= 1:
        return False

        for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False

    return True

#codigo refatorado com comentários

import math


def is_prime(n: int) -> bool:
    """
    Verifica se um número inteiro é primo.

    Um número primo é aquele maior que 1 que não possui
    divisores além de 1 e ele mesmo.

    Args:
        n (int): O número a ser verificado.

    Returns:
        bool: True se n for primo, False caso contrário.

    Examples:
        >>> is_prime(7)
        True
        >>> is_prime(10)
        False
    """

    # Caso base: primos são estritamente maiores que 1
    if n <= 1:
        return False

    # 2 é o único primo par — tratado separadamente para
    # permitir que o loop seguinte pule todos os pares
    if n == 2:
        return True

    # Elimina imediatamente qualquer outro número par
    if n % 2 == 0:
        return False

    # Verifica apenas divisores ímpares até √n.
    # Qualquer fator maior que √n teria um par menor que √n,
    # então não é necessário ir além desse limite.
    limite = math.isqrt(n)  # equivalente a int(n**0.5), porém exato para inteiros
    for divisor in range(3, limite + 1, 2):  # passo 2 → só ímpares
        if n % divisor == 0:
            return False

    # Nenhum divisor encontrado → n é primo
    return True
