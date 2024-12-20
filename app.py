# %%

from collections import Counter
from constants import RANKS, SUITS, STRENGTH_ORDER
from Deck import Deck

deck = Deck()


def evaluate_hand(mao):
    """Avalia uma mão de poker e retorna a melhor combinação."""
    ranks_mao = sorted([RANKS.index(carta[0]) for carta in mao], reverse=True)
    suits_mao = [carta[1] for carta in mao]

    # Funções auxiliares para verificar combinações
    def is_flush():
        return len(set(suits_mao)) == 1

    def is_straight():
        unique_ranks = sorted(list(set(ranks_mao)), reverse=True)
        if len(unique_ranks) < 5:
            return False
        # Verifica sequências normais
        for i in range(len(unique_ranks) - 4):
            if all(unique_ranks[i+j] == unique_ranks[i] - j for j in range(5)):
                return True

    rank_counts = Counter(ranks_mao)
    counts = sorted(rank_counts.values(), reverse=True)

    if is_flush() and is_straight():
        return "Straight Flush"
    if counts[0] == 4:
        return "Four of a Kind"
    if counts[0] == 3 and counts[1] == 2:
        return "Full House"
    if is_flush():
        return "Flush"
    if is_straight():
        return "Straight"
    if counts[0] == 3:
        return "Three of a Kind"
    if counts[0] == 2 and counts[1] == 2:
        return "Two Pair"
    if counts[0] == 2:
        return "One Pair"
    return "High Card"


def evaluate(mao_jogador, board):
    """Avalia a melhor mão de 5 cartas combinando a mão do jogador e o board."""
    from itertools import combinations
    todas_as_cartas = mao_jogador + board
    melhor_combinacao = "High Card"  # Valor inicial
    combinacoes = combinations(todas_as_cartas, 5)

    def valor_combinacao(combinacao_str):
        ordem = STRENGTH_ORDER
        return ordem.index(combinacao_str)

    for combinacao in combinacoes:
        resultado = evaluate_hand(list(combinacao))
        if valor_combinacao(resultado) > valor_combinacao(melhor_combinacao):
            melhor_combinacao = resultado
    return melhor_combinacao


def get_winner(players_hands, board):
    """Retorna o jogador com a melhor mão de poker."""
    return max(players_hands, key=lambda x: STRENGTH_ORDER.index(evaluate(x, board)))


def get_winner_index(players_hands, board):
    return players_hands.index(get_winner(players_hands, board))


def exibir_cartas(cartas):
    """Exibe uma mão de cartas formatada."""
    return " ".join(exibir_carta(carta) for carta in cartas)


def exibir_carta(carta):
    """Exibe uma carta formatada."""
    return carta[0] + carta[1]


def exibir_mao(mao):
    """Exibe uma mão de cartas formatada."""
    return " ".join(exibir_carta(carta) for carta in mao)


mao_jogador = [('A', 'H'), ('A', 'S')]
print("\nMinha mao")
print(mao_jogador)
deck.remove_from_deck(mao_jogador)

player_2 = deck.pick_random_cards()
print("\nPlayer 2")
print(player_2)


board = deck.pick_random_cards(5)


evaluation = evaluate(mao_jogador, board)
player_2_evaluation = evaluate(player_2, board)


winner_index = get_winner_index([mao_jogador, player_2], board)
winner_hand = get_winner([mao_jogador, player_2], board)
print("\nWinner: ", winner_index)
print(f"""
    Player 1: {exibir_mao(mao_jogador)} ({evaluation})
    Player 2: {exibir_mao(player_2)} ({player_2_evaluation})
    Board: {exibir_mao(board)}
    Winner: {exibir_mao(winner_hand)}""")


# %%
