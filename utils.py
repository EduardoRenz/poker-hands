SIMBOL_MAP = {
    "H": "♥",
    "D": "♦",
    "C": "♣",
    "S": "♠",
    "T": "10",
}


def show_cards(cartas):
    """Show formated cards."""
    return " ".join(show_card(carta) for carta in cartas)


def show_card(carta):
    """Show one card formated."""
    return carta[0] + SIMBOL_MAP[carta[1]]
