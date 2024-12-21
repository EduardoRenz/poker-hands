# %%


from constants import RANKS, STRENGTH_ORDER, NUMERAL_RANKS
from Deck import Deck
from Game import Game

deck = Deck()
game = Game()


def get_winner_index(players_hands, board):
    winner = game.get_winner(players_hands, board)
    if winner is None:
        return None
    return players_hands.index(winner)


def exibir_cartas(cartas):
    """Exibe uma mão de cartas formatada."""
    return " ".join(exibir_carta(carta) for carta in cartas)


def exibir_carta(carta):
    """Exibe uma carta formatada."""
    return carta[0] + carta[1]


def exibir_mao(mao):
    """Exibe uma mão de cartas formatada."""
    return " ".join(exibir_carta(carta) for carta in mao)


if __name__ == "__main__":

    mao_jogador = [('A', 'H'), ('A', 'S')]
    print("\nMinha mao")
    print(mao_jogador)
    deck.remove_from_deck(mao_jogador)

    player_2 = deck.pick_random_cards()
    print("\nPlayer 2")
    print(player_2)

    board = deck.pick_random_cards(5)

    evaluation = game.evaluate(mao_jogador, board)
    player_2_evaluation = game.evaluate(player_2, board)

    winner_index = get_winner_index([mao_jogador, player_2], board)
    winner_hand = game.get_winner([mao_jogador, player_2], board)
    print("\nWinner: ", winner_index)
    print(f"""
        Player 1: {exibir_mao(mao_jogador)} ({evaluation})
        Player 2: {exibir_mao(player_2)} ({player_2_evaluation})
        Board: {exibir_mao(board)}
        Winner: {exibir_mao(winner_hand)}""")


# %%
