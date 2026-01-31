def ler_int(mensagem):
    valor = input(mensagem).strip()

    if not valor:
        raise ValueError('Valor obrigatório')

    if not valor.isdigit():
        raise ValueError('Apenas números inteiros são aceitos')

    return int(valor)
