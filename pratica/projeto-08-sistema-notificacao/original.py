# Função auxiliar para verificar se a condição crítica foi atingida
def verificar_condicao(valor, limite_critico):
    """
    Retorna True se o valor ultrapassar o limite crítico.
    """
    return valor >= limite_critico


# Função auxiliar para disparar alerta no console
def disparar_alerta_console(mensagem):
    """
    Exibe uma mensagem de alerta no console.
    """
    print(f"[ALERTA] {mensagem}")


# Função auxiliar para simular envio de alerta por e-mail
def disparar_alerta_email(mensagem, destinatario="admin@sistema.com"):
    """
    Simula envio de e-mail de alerta.
    """
    print(f"[EMAIL SIMULADO] Para: {destinatario}\nMensagem: {mensagem}\n")


# Função principal que integra a lógica
def monitorar_sistema(valor_atual, limite_critico):
    """
    Monitora o valor e dispara alerta apenas se condição crítica for atingida.
    """
    if verificar_condicao(valor_atual, limite_critico):
        mensagem = f"Condição crítica atingida! Valor = {valor_atual}, Limite = {limite_critico}"
        disparar_alerta_console(mensagem)
        disparar_alerta_email(mensagem)
    else:
        print(f"Valor {valor_atual} dentro dos limites normais.")


# Exemplo de uso
if __name__ == "__main__":
    # Simulação de valores monitorados
    valores = [45, 60, 75, 90, 120]
    limite = 100

    for v in valores:
        monitorar_sistema(v, limite)




# Refatoração do codigo


def condicao_critica(valor, limite):
    """Retorna True se o valor atingir ou ultrapassar o limite crítico."""
    return valor >= limite


def alerta(mensagem, destinatario="admin@sistema.com"):
    """Dispara alerta no console e simula envio de e-mail."""
    print(f"[ALERTA] {mensagem}")
    print(f"[EMAIL SIMULADO] Para: {destinatario}\nMensagem: {mensagem}\n")


def monitorar(valor, limite):
    """Monitora o valor e dispara alerta apenas se condição crítica for atingida."""
    if condicao_critica(valor, limite):
        mensagem = f"Condição crítica atingida! Valor = {valor}, Limite = {limite}"
        alerta(mensagem)
    else:
        print(f"Valor {valor} dentro dos limites normais.")


if __name__ == "__main__":
    # Simulação de valores monitorados
    valores = [45, 60, 75, 90, 120]
    limite = 100

    for v in valores:
        monitorar(v, limite)
