def exibir_cartas(cartas):
    """Exibe uma mão de cartas formatada."""
    return " ".join(exibir_carta(carta) for carta in cartas)


def exibir_carta(carta):
    """Exibe uma carta formatada."""
    return carta[0] + carta[1]


def exibir_mao(mao):
    """Exibe uma mão de cartas formatada."""
    return " ".join(exibir_carta(carta) for carta in mao)
